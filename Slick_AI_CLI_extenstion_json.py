// === slick_ai_cli_extensions_json.py ===
// This version uses a JSON config file to define CLI commands dynamically

import argparse
import json
import importlib
import os

CONFIG_PATH = "cli_extensions/cli_config.json"

def load_config():
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"❌ CLI config JSON not found at: {CONFIG_PATH}")
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def execute_command(command_def, args):
    module_path = command_def["module"]
    function_name = command_def["function"]
    Module = importlib.import_module(module_path)
    handler = getattr(Module, function_name)
    handler(args)

def main():
    config = load_config()
    parser = argparse.ArgumentParser(description="🧠 Slick AI JSON CLI")
    subparsers = parser.add_subparsers(dest="command")

    for command_name, command_def in config["commands"].items():
        subparser = subparsers.add_parser(command_name, help=command_def.get("help", ""))
        for arg in command_def.get("arguments", []):
            subparser.add_argument(arg["flag"], **arg["options"])
        subparser.set_defaults(command_def=command_def)

    args = parser.parse_args()
    if hasattr(args, "command_def"):
        execute_command(args.command_def, args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
