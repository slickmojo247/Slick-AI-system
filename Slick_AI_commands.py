# === slick_ai_cli_extensions.py ===
# CLI extension script for Slick AI with custom command mappings and logic routing

import argparse
import sys
from slick_ai.logic.session_tools.logic_loader import LogicLoader
from slick_ai.logic.session_tools.memory_trainer import MemoryTrainer
from slick_ai.logic.session_tools.logic_session_logger import SessionLogger


def handle_check_syntax(args):
    print(f"\n🔍 Running syntax check on: {args.file}")
    loader = LogicLoader()
    results = loader.check_syntax(args.file)
    for line in results:
        print(line)


def handle_inspect_logic(args):
    print(f"\n📘 Inspecting logic in: {args.file}")
    loader = LogicLoader()
    filtered = loader.inspect_logic(args.file, version=args.version, grade=args.grade, tag=args.tag)
    for entry in filtered:
        print(entry)


def handle_train_memory(args):
    print(f"\n🧠 Training memory from: {args.file}")
    trainer = MemoryTrainer()
    trainer.train_from_csv(args.file, version=args.version, grade=args.grade)


def handle_apply_cohesion(args):
    print(f"\n🔗 Applying logic cohesion from: {args.file}")
    loader = LogicLoader()
    session_data = loader.build_session(args.file)
    logger = SessionLogger()
    logger.save(session_data, args.output)


def main():
    parser = argparse.ArgumentParser(description="🧠 Slick AI CLI Extension")
    subparsers = parser.add_subparsers(dest="command")

    # check-syntax command
    syntax_parser = subparsers.add_parser("check-syntax", help="Check logic syntax for tagged CSV")
    syntax_parser.add_argument("--file", required=True, help="Path to CSV file")
    syntax_parser.set_defaults(func=handle_check_syntax)

    # inspect-logic command
    inspect_parser = subparsers.add_parser("inspect-logic", help="Filter and view logic")
    inspect_parser.add_argument("--file", required=True)
    inspect_parser.add_argument("--version")
    inspect_parser.add_argument("--grade")
    inspect_parser.add_argument("--tag")
    inspect_parser.set_defaults(func=handle_inspect_logic)

    # train-memory command
    memory_parser = subparsers.add_parser("train-memory", help="Inject logic into memory")
    memory_parser.add_argument("--file", required=True)
    memory_parser.add_argument("--version")
    memory_parser.add_argument("--grade")
    memory_parser.set_defaults(func=handle_train_memory)

    # apply-cohesion command
    cohesion_parser = subparsers.add_parser("apply-cohesion", help="Build session file from logic")
    cohesion_parser.add_argument("--file", required=True)
    cohesion_parser.add_argument("--output", default="sessions/cohesion_session.json")
    cohesion_parser.set_defaults(func=handle_apply_cohesion)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
