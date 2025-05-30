from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

class MapServer:
    def __init__(self):
        self.app = FastAPI()
    
    def Start(self, ip = 'localhost', port = 7777):
        self.app.mount("/", StaticFiles(directory = "maps", html = True))
        uvicorn.run(self.app, host = ip, port = port)