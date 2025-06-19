from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class APIAdapter:
    def __init__(self):
        self.app = FastAPI()
        self._register_routes()
    
    def _register_routes(self):
        @self.app.get("/v1/query")
        async def legacy_query(q: str):
            return {"response": "Legacy format"}
            
        @self.app.get("/v2/query")
        async def modern_query(q: str):
            return {"data": {"response": "Modern format"}}
