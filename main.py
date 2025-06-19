#!/usr/bin/env python3
"""
SLICK AI v2.1 - Main Entry Point
"""

import cmd
import logging
from engine.SlickLogicEngine import SlickLogicEngine
from memory.MemoryBank import MemoryBank
from ai_core.APIOrchestrator import APIOrchestrator

class SlickCLI(cmd.Cmd):
    prompt = "SLICK> "
    intro = "SLICK AI System - Type 'help' for commands\n"
    
    def __init__(self):
        super().__init__()
        self._init_system()
        
    def _init_system(self):
        """Initialize all components"""
        self.logger = self._setup_logging()
        self.memory = MemoryBank()
        self.orchestrator = APIOrchestrator()
        self.engine = SlickLogicEngine(self.memory)
        self.logger.info("System initialized")

    def _setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler("slick.log"),
                logging.StreamHandler()
            ]
        )
        return logging.getLogger(__name__)

    def default(self, line):
        """Handle natural language input"""
        if line.lower().startswith(('what', 'how', 'why', 'when', 'where')):
            self.do_query(line)
        else:
            print("Type 'query' before your question or 'help' for commands")

    def do_query(self, arg):
        """Process a query: QUERY <your question> or just ask naturally"""
        try:
            result = self.engine.process(arg)
            response = self.orchestrator.route(result)
            print(f"\n{response}\n")
        except Exception as e:
            self.logger.error(f"Query failed: {e}")
            print(f"Error: {e}")

    def do_mode(self, arg):
        """Change personality mode: MODE <balanced|technical|creative|homer>"""
        try:
            self.engine.set_mode(arg)
            print(f"Mode set to {arg}")
        except ValueError as e:
            print(f"Error: {e}")

    def do_exit(self, arg):
        """Exit the system"""
        self.logger.info("Shutdown initiated")
        print("System shutting down...")
        return True

if __name__ == "__main__":
    SlickCLI().cmdloop()
