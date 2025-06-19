from connectors.ai import AIConnector
import asyncio

async def send_message(query: str):
    ai = AIConnector()
    await ai.init()
    return await ai.process(query)
