import sys
from slick_cli.commands import all_commands

def main():
    if len(sys.argv) < 2:
        print("Available commands:")
        for cmd in all_commands:
            print(f"- {cmd.__name__}")
        sys.exit(0)

    command_name = sys.argv[1]
    args = sys.argv[2:]

    for cmd in all_commands:
        if cmd.__name__.replace("_", "-") == command_name:
            cmd(args)
            return

    print(f"❌ Unknown command: {command_name}")
    print("Available commands:")
    for cmd in all_commands:
        print(f"- {cmd.__name__}")
