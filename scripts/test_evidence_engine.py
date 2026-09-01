#!/usr/bin/env python3
"""
Unit tests for the ShipLift Evidence Engine (evidence_engine.py).

Run: python3 scripts/test_evidence_engine.py
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import evidence_engine as engine  # noqa: E402


def ev(id_, category, description, date, source="user", metadata=None, links=None, impact="Unknown"):
    return {
        "id": id_,
        "company": "acme",
        "category": category,
        "description": description,
        "date": date,
        "source": source,
        "confidence": "High",
        "metadata": metadata or {},
        "links": links or [],
        "impact": impact,
    }


class LinkingTests(unittest.TestCase):
    def test_related_evidence_is_linked_by_keyword_and_date(self):
        a = ev("a", "Investigation", "Investigated flaky Cypress tests", "2026-08-10")
        b = ev("b", "Code Review", "Fixed the Cypress flaky test setup", "2026-08-12", source="git")
        score, reasons = engine.link_score(a, b)
        self.assertGreaterEqual(score, engine.LINK_SCORE_THRESHOLD)
        self.assertTrue(reasons)

    def test_unrelated_evidence_is_not_linked(self):
        a = ev("a", "Documentation", "Updated onboarding docs", "2026-08-01")
        b = ev("b", "Investigation", "Investigated flaky Cypress tests", "2026-08-30")
        score, _ = engine.link_score(a, b)
        self.assertLess(score, engine.LINK_SCORE_THRESHOLD)

    def test_different_companies_never_link(self):
        a = ev("a", "Investigation", "Investigated flaky Cypress tests", "2026-08-10")
        b = dict(ev("b", "Investigation", "Investigated flaky Cypress tests", "2026-08-10"))
        b["company"] = "beta"
        score, _ = engine.link_score(a, b)
        self.assertEqual(score, 0)

    def test_find_related_returns_sorted_candidates(self):
        target = ev("a", "Investigation", "Investigated flaky Cypress tests in CI", "2026-08-10")
        items = [
            target,
            ev("b", "Code Review", "Fixed Cypress flaky test CI issue", "2026-08-11", source="git"),
            ev("c", "Documentation", "Wrote onboarding guide", "2026-01-01"),
        ]
        related = engine.find_related(items, target)
        ids = [c["id"] for c in related]
        self.assertIn("b", ids)
        self.assertNotIn("c", ids)

    def test_uncertain_relationship_stays_separate(self):
        # Same company, far apart in time, no shared keywords -> no link.
        a = ev("a", "Collaboration", "Helped Ahmed with a rendering bug", "2026-01-05")
        b = ev("b", "Planning", "Discussed roadmap priorities", "2026-06-20")
        score, _ = engine.link_score(a, b)
        self.assertLess(score, engine.LINK_SCORE_THRESHOLD)


class StrengthTests(unittest.TestCase):
    def test_strong_evidence_multi_source_plus_metric(self):
        items = [
            ev("a", "Investigation", "Investigated flaky tests", "2026-08-01", source="pulse"),
            ev("b", "Code Review", "Fixed flaky tests", "2026-08-02", source="git",
               metadata={"before": "12 flaky", "after": "0 flaky"}),
        ]
        level, _ = engine.evidence_strength(items)
        self.assertEqual(level, "Strong Evidence")

    def test_moderate_evidence_repeated_no_metric(self):
        items = [
            ev(str(i), "Code Review", f"Reviewed PR {i}", "2026-08-0" + str(i), source="user")
            for i in range(1, 4)
        ]
        level, _ = engine.evidence_strength(items)
        self.assertEqual(level, "Moderate Evidence")

    def test_early_signal_isolated_activity(self):
        items = [ev("a", "Code Review", "Reviewed a PR", "2026-08-01")]
        level, _ = engine.evidence_strength(items)
        self.assertEqual(level, "Early Signal")

    def test_no_evidence_is_early_signal(self):
        level, reasons = engine.evidence_strength([])
        self.assertEqual(level, "Early Signal")
        self.assertIn("no evidence", reasons)


class ImpactTests(unittest.TestCase):
    def test_measured_impact_from_metric(self):
        item = ev("a", "Code Review", "Improved coverage", "2026-08-01",
                   metadata={"coverage_before": "72%", "coverage_after": "84%"})
        level, _ = engine.impact_level(item)
        self.assertEqual(level, "Measured")

    def test_observed_impact_from_description(self):
        item = ev("a", "Knowledge Sharing", "The team adopted the new testing pattern", "2026-08-01")
        level, _ = engine.impact_level(item)
        self.assertEqual(level, "Observed")

    def test_supported_impact_for_unblocking(self):
        item = ev("a", "Unblocking", "Helped unblock a teammate on the deploy pipeline", "2026-08-01")
        level, _ = engine.impact_level(item)
        self.assertEqual(level, "Supported")

    def test_unknown_impact_default(self):
        item = ev("a", "Code Review", "Reviewed 3 PRs", "2026-08-01", metadata={"pr_count": 3})
        # pr_count IS a measurable metadata key in this engine, so this
        # counts as Measured; use a category/description with no metric at all.
        plain = ev("b", "Technical Decision", "Discussed the approach", "2026-08-01")
        level, _ = engine.impact_level(plain)
        self.assertEqual(level, "Unknown")


class SignalTests(unittest.TestCase):
    def test_recurring_pattern_is_detected(self):
        items = [
            ev(str(i), "Code Review", f"Reviewed PR {i}", f"2026-08-0{i}")
            for i in range(1, 4)
        ]
        signals = engine.detect_signals(items)
        self.assertEqual(len(signals), 1)
        self.assertEqual(signals[0]["category"], "Code Review")
        self.assertEqual(signals[0]["occurrences"], 3)

    def test_isolated_activity_is_not_a_signal(self):
        items = [ev("a", "Mentoring", "Helped onboard a new hire", "2026-08-01")]
        signals = engine.detect_signals(items)
        self.assertEqual(signals, [])


class BlindSpotTests(unittest.TestCase):
    def test_missing_category_is_limited_evidence_not_a_judgment(self):
        items = [ev("a", "Feature Delivery", "Shipped settings page", "2026-08-01")]
        areas = engine.blind_spots(items)
        mentoring = next(a for a in areas if a["area"] == "Mentoring")
        self.assertEqual(mentoring["level"], "Limited Evidence")
        self.assertEqual(mentoring["evidence_count"], 0)

    def test_repeated_category_is_strong_evidence(self):
        items = [ev(str(i), "Mentoring", "Mentored a junior engineer", f"2026-08-0{i}") for i in range(1, 4)]
        areas = engine.blind_spots(items)
        mentoring = next(a for a in areas if a["area"] == "Mentoring")
        self.assertEqual(mentoring["level"], "Strong Evidence")


class AntiInflationTests(unittest.TestCase):
    def test_flags_unsupported_percentage(self):
        item = ev("a", "Code Review", "Improved team productivity by 30%", "2026-08-01")
        findings = engine.lint_evidence(item)
        self.assertTrue(findings)

    def test_flags_unsupported_business_outcome(self):
        item = ev("a", "Collaboration", "Helped teammate, increased team velocity", "2026-08-01")
        findings = engine.lint_evidence(item)
        self.assertTrue(any("business" in f["issue"] or "productivity" in f["issue"] for f in findings))

    def test_flags_unsupported_leadership_claim(self):
        item = ev("a", "Initiative", "Led the testing initiative", "2026-08-01")
        findings = engine.lint_evidence(item)
        self.assertTrue(findings)

    def test_flags_unsupported_team_size_claim(self):
        item = ev("a", "Mentoring", "Led a team of 5 engineers", "2026-08-01")
        findings = engine.lint_evidence(item)
        self.assertTrue(findings)

    def test_measurable_claim_is_not_flagged(self):
        item = ev("a", "Code Review", "Improved coverage by 12 percentage points", "2026-08-01",
                   metadata={"coverage_before": "72%", "coverage_after": "84%"})
        findings = engine.lint_evidence(item)
        self.assertEqual(findings, [])

    def test_plain_fact_is_not_flagged(self):
        item = ev("a", "Code Review", "Reviewed 3 PRs", "2026-08-01", metadata={"pr_count": 3})
        findings = engine.lint_evidence(item)
        self.assertEqual(findings, [])


class OpenThreadTests(unittest.TestCase):
    def test_unresolved_investigation_is_an_open_thread(self):
        items = [ev("a", "Investigation", "Started investigating Cypress instability", "2026-08-01")]
        threads = engine.open_threads(items)
        self.assertEqual(len(threads), 1)
        self.assertIn("Cypress", threads[0]["follow_up_question"])

    def test_linked_resolution_closes_the_thread(self):
        items = [
            ev("a", "Investigation", "Started investigating Cypress instability", "2026-08-01",
               links=["b"]),
            ev("b", "Investigation", "Found the root cause and fixed Cypress flakiness", "2026-08-10"),
        ]
        threads = engine.open_threads(items)
        self.assertEqual(threads, [])

    def test_resolved_metadata_flag_closes_the_thread(self):
        items = [ev("a", "Initiative", "Started frontend testing initiative", "2026-08-01",
                     metadata={"resolved": True})]
        threads = engine.open_threads(items)
        self.assertEqual(threads, [])

    def test_non_open_category_is_not_a_thread(self):
        items = [ev("a", "Code Review", "Reviewed 3 PRs", "2026-08-01")]
        threads = engine.open_threads(items)
        self.assertEqual(threads, [])


if __name__ == "__main__":
    unittest.main()
