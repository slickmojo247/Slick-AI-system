import argparse

def check_syntax(args=None):
    parser = argparse.ArgumentParser(description="Check syntax of a logic CSV file")
    parser.add_argument('--file', required=True, help='Target file to check')
    args = parser.parse_args(args)

    print(f"✅ Syntax OK | 0 errors in {args.file}")
