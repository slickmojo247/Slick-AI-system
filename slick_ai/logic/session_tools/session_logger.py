import aiofiles
import csv
from datetime import datetime
import os

class SessionLogger:
    async def log(self, prompt: str, response: str):
        session_file = "sessions/session_log.csv"
        os.makedirs(os.path.dirname(session_file), exist_ok=True)
        async with aiofiles.open(session_file, mode='a') as f:
            writer = csv.writer(f)
            await writer.writerow([datetime.now(), prompt, response])
        print(f"📝 Logged to {session_file}")
