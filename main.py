from fastapi import FastAPI, Request
from agent import entry_point

app = FastAPI()

@app.post("/agent")
async def handle_agent(request: Request):
    data = await request.json()
    return entry_point(data)