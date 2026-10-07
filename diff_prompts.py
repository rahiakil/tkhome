import sys
import os
import difflib
from config import DEFAULT_SYSTEM_PROMPT

# ANSI terminal colors
GREEN = '\033[0;32m'
RED = '\033[0;31m'
BLUE = '\033[0;34m'
YELLOW = '\033[0;33m'
CYAN = '\033[0;36m'
BOLD = '\033[1m'
NC = '\033[0m'

def main():
    optimized_path = "optimized_system_prompt.txt"
    
    if not os.path.exists(optimized_path):
        print(f"\n{YELLOW}💡 No optimized system prompt found yet (optimized_system_prompt.txt doesn't exist).")
        print(f"The pipeline is currently using the DEFAULT system prompt defined in config.py.{NC}")
        print("\n=== CURRENT BASELINE SYSTEM PROMPT ===")
        print(DEFAULT_SYSTEM_PROMPT)
        return

    with open(optimized_path, "r") as f:
        optimized_prompt = f.read()

    if DEFAULT_SYSTEM_PROMPT.strip() == optimized_prompt.strip():
        print(f"\n{CYAN}{BOLD}✅ Prompt Status: Both system prompts are currently IDENTICAL.{NC}")
        print(f"{YELLOW}The Meta-Prompt Optimizer has not written any differences yet, or the last optimization iteration did not surpass the validation baseline.{NC}")
        print(f"\nTo let the Meta-Optimizer generate self-improved instructions, run:")
        print(f"  {BOLD}python3 run.py --optimize{NC} or choose {BOLD}Option [4]{NC} in the TUI.")
        print(f"\n{BLUE}=== CURRENT SYSTEM PROMPT (baseline) ==={NC}")
        print(DEFAULT_SYSTEM_PROMPT)
        return

    print(f"\n{GREEN}{BOLD}🔍 DIFFERENCES ADDED BY THE META-PROMPT OPTIMIZER:{NC}")
    print(f"This comparison shows rules appended/modified by the self-improving loop ({RED}- baseline{NC} vs {GREEN}+ optimized{NC}):")
    print(f"{BLUE}================================================================================{NC}")

    # Generate a line-by-line colored diff
    diff = difflib.ndiff(DEFAULT_SYSTEM_PROMPT.splitlines(), optimized_prompt.splitlines())
    
    for line in diff:
        if line.startswith('+ '):
            print(f"{GREEN}{line}{NC}")
        elif line.startswith('- '):
            print(f"{RED}{line}{NC}")
        elif line.startswith('? '):
            # skips intra-line guidance helper line
            continue
        else:
            # show context lines slightly dimmed
            print(f"\033[0;90m{line}\033[0m")
            
    print(f"{BLUE}================================================================================{NC}")

if __name__ == "__main__":
    main()
