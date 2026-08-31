#!/bin/bash

# ShipLift Git Analysis Helper Script
# This script provides repository snapshots to assist with ShipLift analysis.
# It does NOT perform the full ShipLift analysis - the AI agent does that.

set -e

# Color codes for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Functions

show_help() {
    cat << EOF
ShipLift Git Analysis Helper

Usage: git-analysis.sh [command] [options]

Commands:

  status              Show current repository status
  log [days]          Show commit log for last N days (default: 7)
  quarter [year-q]    Show commits for a quarter (e.g., 2024-Q3)
  branches            Show recent branches
  prs [days]          Show recent PR information
  stats [days]        Show repository statistics
  diff [ref1] [ref2]  Show diff between references
  tags                Show recent tags
  help                Show this help message

Options:
  -j, --json          Output in JSON format
  -r, --repo PATH     Specify repository path (default: current)
  -v, --verbose       Verbose output

Examples:

  ./git-analysis.sh status
  ./git-analysis.sh log 30
  ./git-analysis.sh quarter 2024-Q3
  ./git-analysis.sh log 7 --verbose
  ./git-analysis.sh branches -r /path/to/repo

EOF
}

# Validate that we're in a git repository
validate_git_repo() {
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        echo "Error: Not in a git repository"
        exit 1
    fi
}

# Show repository status
cmd_status() {
    echo -e "${BLUE}Repository Status${NC}"
    echo "Repository: $(git rev-parse --show-toplevel)"
    echo "Branch: $(git rev-parse --abbrev-ref HEAD)"
    echo "Last Commit: $(git log -1 --format='%h - %s (%ar)')"
    echo ""
    echo -e "${BLUE}Uncommitted Changes:${NC}"
    git status --short || echo "No changes"
}

# Show commit log
cmd_log() {
    local days=${1:-7}
    local since="$days.days.ago"
    
    echo -e "${BLUE}Commits from last ${days} days:${NC}"
    echo ""
    
    git log --since="$since" --oneline --decorate --graph || echo "No commits found"
}

# Show quarter commits
cmd_quarter() {
    local quarter=${1:-current}
    
    if [[ "$quarter" == "current" ]]; then
        # Calculate current quarter
        local month=$(date +%m)
        local year=$(date +%Y)
        if (( month <= 3 )); then
            quarter="${year}-Q1"
            since="${year}-01-01"
            until="${year}-03-31"
        elif (( month <= 6 )); then
            quarter="${year}-Q2"
            since="${year}-04-01"
            until="${year}-06-30"
        elif (( month <= 9 )); then
            quarter="${year}-Q3"
            since="${year}-07-01"
            until="${year}-09-30"
        else
            quarter="${year}-Q4"
            since="${year}-10-01"
            until="${year}-12-31"
        fi
    else
        # Parse quarter format (YYYY-QN)
        if [[ ! $quarter =~ ^[0-9]{4}-Q[1-4]$ ]]; then
            echo "Error: Quarter format should be YYYY-QN (e.g., 2024-Q3)"
            exit 1
        fi
        
        local year=$(echo $quarter | cut -d- -f1)
        local q=$(echo $quarter | cut -d- -f2 | grep -oE '[0-9]')
        
        case $q in
            1) since="${year}-01-01"; until="${year}-03-31" ;;
            2) since="${year}-04-01"; until="${year}-06-30" ;;
            3) since="${year}-07-01"; until="${year}-09-30" ;;
            4) since="${year}-10-01"; until="${year}-12-31" ;;
        esac
    fi
    
    echo -e "${BLUE}Commits for ${quarter}:${NC}"
    echo -e "${YELLOW}Period: ${since} to ${until}${NC}"
    echo ""
    
    git log --since="$since" --until="$until" --oneline --decorate --graph || echo "No commits found"
}

# Show recent branches
cmd_branches() {
    echo -e "${BLUE}Recent Branches:${NC}"
    git for-each-ref --sort=-committerdate refs/heads/ --format='%(refname:short) - %(committerdate:short) - %(authorname)'
}

# Show repository statistics
cmd_stats() {
    local days=${1:-7}
    local since="$days.days.ago"
    
    echo -e "${BLUE}Repository Statistics (last ${days} days):${NC}"
    echo ""
    
    local commit_count=$(git log --since="$since" --oneline | wc -l)
    echo "Total commits: $commit_count"
    
    echo ""
    echo -e "${BLUE}Contributors:${NC}"
    git log --since="$since" --format='%aN' | sort | uniq -c | sort -rn
    
    echo ""
    echo -e "${BLUE}Files Changed:${NC}"
    git diff --name-only --since="$since" HEAD | sort | uniq -c | sort -rn | head -10
    
    echo ""
    echo -e "${BLUE}Commits by Day:${NC}"
    git log --since="$since" --format='%aI' | cut -d'T' -f1 | sort | uniq -c
}

# Show diff between references
cmd_diff() {
    local ref1=${1:-HEAD~1}
    local ref2=${2:-HEAD}
    
    echo -e "${BLUE}Diff: ${ref1}...${ref2}${NC}"
    echo ""
    
    # Summary
    git diff --stat "$ref1" "$ref2"
    
    echo ""
    echo -e "${BLUE}Detailed Changes:${NC}"
    git diff "$ref1" "$ref2" | head -100
    echo ""
    echo "(showing first 100 lines)"
}

# Show recent tags
cmd_tags() {
    echo -e "${BLUE}Recent Tags:${NC}"
    git tag -l --sort=-version:refname | head -20
}

# Main script logic

validate_git_repo

# Parse command
command=${1:-help}

case "$command" in
    status)
        cmd_status
        ;;
    log)
        cmd_log "$2"
        ;;
    quarter)
        cmd_quarter "$2"
        ;;
    branches)
        cmd_branches
        ;;
    stats)
        cmd_stats "$2"
        ;;
    diff)
        cmd_diff "$2" "$3"
        ;;
    tags)
        cmd_tags
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo "Unknown command: $command"
        echo "Use 'git-analysis.sh help' for usage information"
        exit 1
        ;;
esac
