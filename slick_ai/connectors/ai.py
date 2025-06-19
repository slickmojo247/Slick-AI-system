import asyncio
from logic.session_tools.session_logger import SessionLogger

class AIConnector:
    async def init(self):
        self.session_logger = SessionLogger()
        print("✅ AIConnector ready (hybrid sessions enabled)")

    async def process(self, query: str):
        response = f"AI processed: {query}"
        await self.session_logger.log(query, response)
        return response
