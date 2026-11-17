import random
import argparse
import sys
PROVERBS = [
    "هر که بامش بگیرد، نیازمند پایی است.",
    "صبر، کلید هر دروازه است.",
    "دست به دست می‌رود، دل‌ها هم می‌چسبد.",
    "زمان می‌گذرد، ولی درس‌ها می‌مانند.",
    "نفرین باش، چون دروازه‌های خسته‌ام."
]
def get_random_proverb():
    """Return a random Persian proverb."""
    return random.choice(PROVERBS)
def main():
    parser = argparse.ArgumentParser(description="Generate a random Persian proverb.")
    parser.add_argument("command", nargs="?", default="generate", help="command to run (generate)")
    args = parser.parse_args()
    if args.command == "generate":
        print(get_random_proverb())
    else:
        parser.print_help()
        sys.exit(1)
if __name__ == "__main__":
    main()
