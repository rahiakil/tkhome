#!/bin/bash

# --- Color Definitions for Premium UI ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Set up clean trap to exit gracefully on Ctrl+C
trap ctrl_c INT
function ctrl_c() {
    echo -e "\n\n${YELLOW}👋 Gracefully exiting TUI. Good luck with the presentation!${NC}\n"
    exit 0
}

# --- Helper Functions ---
function show_header() {
    clear
    echo -e "${BLUE}${BOLD}================================================================================${NC}"
    echo -e "         ${CYAN}${BOLD}⚡ VERTEX SMART CATEGORIZATION ENGINE - INTERACTIVE TUI ⚡${NC}"
    echo -e "                   ${BLUE}Lead AI Product Engineering Dashboard${NC}"
    echo -e "${BLUE}${BOLD}================================================================================${NC}"
    echo -e "Today's Date: $(date)"
    echo -e "Repository:   https://github.com/rahiakil/tkhome"
    echo -e "${BLUE}${BOLD}--------------------------------------------------------------------------------${NC}"
}

function press_any_key() {
    echo ""
    echo -e "${YELLOW}Press any key to return to the main menu...${NC}"
    read -n 1 -s -r
}

# --- Main Menu Loop ---
while true; do
    show_header
    
    # Check if .env with API key is available
    if [ -f .env ] && grep -q "OPENAI_API_KEY" .env; then
        echo -e "🔑 OpenAI API Status: ${GREEN}${BOLD}CONNECTED${NC} (Found .env key)"
    else
        echo -e "🔑 OpenAI API Status: ${RED}${BOLD}NOT CONNECTED${NC} (Missing .env key, only Option 1 will work)"
    fi
    echo -e "${BLUE}${BOLD}--------------------------------------------------------------------------------${NC}"
    
    echo -e "Please select an operational pipeline command to run:\n"
    echo -e "  ${CYAN}${BOLD}[1]${NC} Run Local Smart Heuristic Baseline  ${YELLOW}(Fast, Free, 100% Offline)${NC}"
    echo -e "  ${CYAN}${BOLD}[2]${NC} Run SOTA OpenAI Production Model    ${YELLOW}(gpt-4o-mini, Concurrently Parallelized)${NC}"
    echo -e "  ${CYAN}${BOLD}[3]${NC} Run SOTA OpenAI on custom files     ${YELLOW}(Specify input/output JSON)${NC}"
    echo -e "  ${CYAN}${BOLD}[4]${NC} Run Automated Prompt Optimizer      ${YELLOW}(Auto-tuned prompt training loop)${NC}"
    echo -e "  ${CYAN}${BOLD}[5]${NC} View Prompt Differences & Changes    ${YELLOW}(Compare baseline vs optimized prompts)${NC}"
    echo -e "  ${CYAN}${BOLD}[6]${NC} Regenerate Visual Browser Report    ${YELLOW}(Rebuilds training_runs_report.md)${NC}"
    echo -e "  ${CYAN}${BOLD}[7]${NC} Display Project Slide Presentation   ${YELLOW}(Preview presentation outline)${NC}"
    echo -e "  ${CYAN}${BOLD}[8]${NC} View Codebase Status & Git Log      ${YELLOW}(Quick git status & commit verification)${NC}"
    echo -e "  ${CYAN}${BOLD}[9]${NC} Exit TUI"
    echo ""
    echo -e "${BLUE}${BOLD}================================================================================${NC}"
    echo -en "${CYAN}${BOLD}Enter choice [1-9]: ${NC}"
    read -r choice

    case $choice in
        1)
            show_header
            echo -e "${GREEN}${BOLD}🚀 Running Local Smart Heuristic Engine...${NC}\n"
            python3 run.py --mode mock
            press_any_key
            ;;
        2)
            show_header
            echo -e "${GREEN}${BOLD}🚀 Running OpenAI Production pipeline (gpt-4o-mini, 10 Threads)...${NC}\n"
            python3 run.py --mode openai
            press_any_key
            ;;
        3)
            show_header
            echo -e "${GREEN}${BOLD}🚀 Run OpenAI Production pipeline on Custom Files${NC}\n"
            echo -en "${YELLOW}Enter path to input search result JSON [default: search_results_ground_truth_train.json]: ${NC}"
            read -r input_path
            if [ -z "$input_path" ]; then
                input_path="search_results_ground_truth_train.json"
            fi
            
            echo -en "${YELLOW}Enter path to save prediction output JSON [default: search_results_predictions.json]: ${NC}"
            read -r output_path
            if [ -z "$output_path" ]; then
                output_path="search_results_predictions.json"
            fi
            
            if [ ! -f "$input_path" ]; then
                echo -e "\n${RED}${BOLD}❌ Error: Input file '$input_path' does not exist!${NC}"
            else
                echo -e "\n${GREEN}Executing: python3 run.py --mode openai --input $input_path --output $output_path${NC}\n"
                python3 run.py --mode openai --input "$input_path" --output "$output_path"
            fi
            press_any_key
            ;;
        4)
            show_header
            echo -e "${GREEN}${BOLD}🚀 Starting Automated Self-Improving Meta-Prompt Optimizer...${NC}\n"
            echo -en "${YELLOW}Enter number of optimization iterations [default: 1]: ${NC}"
            read -r iterations
            if [ -z "$iterations" ]; then
                iterations=1
            fi
            echo -en "${YELLOW}Enter number of validation products to sample [default: 15]: ${NC}"
            read -r opt_limit
            if [ -z "$opt_limit" ]; then
                opt_limit=15
            fi
            echo -e "\n${GREEN}Executing: python3 run.py --optimize --iterations $iterations --opt-limit $opt_limit${NC}\n"
            python3 run.py --optimize --iterations "$iterations" --opt-limit "$opt_limit"
            press_any_key
            ;;
        5)
            show_header
            echo -e "${GREEN}${BOLD}🚀 Comparing Baseline vs Optimized Prompts...${NC}\n"
            python3 diff_prompts.py
            press_any_key
            ;;
        6)
            show_header
            echo -e "${GREEN}${BOLD}🚀 Generating Markdown Browser Dashboard Report...${NC}\n"
            python3 generate_report.py
            echo -e "\n${GREEN}${BOLD}✅ Successfully generated 'training_runs_report.md'!${NC}"
            echo -e "You can now view this instantly rendered in GitHub at:"
            echo -e "${CYAN}https://github.com/rahiakil/tkhome/blob/main/training_runs_report.md${NC}"
            press_any_key
            ;;
        7)
            show_header
            echo -e "${GREEN}${BOLD}📋 Showing Quick Presentation Slide Overview...${NC}\n"
            if [ -f presentation_slides.md ]; then
                # Show first 45 lines of the presentation
                head -n 45 presentation_slides.md
                echo -e "\n${YELLOW}... [Review presentation_slides.md in your repository for the complete presentation] ...${NC}"
            else
                echo -e "${RED}❌ Error: 'presentation_slides.md' not found.${NC}"
            fi
            press_any_key
            ;;
        8)
            show_header
            echo -e "${GREEN}${BOLD}📋 Current Codebase status & Remote Git branches:${NC}\n"
            git status
            echo -e "\n${BLUE}${BOLD}--- Recent 3 Commits on GitHub ---${NC}"
            git log -n 3 --oneline
            press_any_key
            ;;
        9)
            echo -e "\n${GREEN}${BOLD}👋 Goodbye and good luck with the presentation!${NC}\n"
            exit 0
            ;;
        *)
            echo -e "\n${RED}${BOLD}❌ Invalid entry! Please enter a number between 1 and 8.${NC}"
            sleep 2
            ;;
    esac
done
