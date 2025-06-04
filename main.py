from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    index_file = Path("index.html")
    return index_file.read_text(encoding="utf-8")
