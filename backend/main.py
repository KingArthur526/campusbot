from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI()

@app.get("/ping")
def ping():
    return {"Shraddha":"sleeping"}

class Ask(BaseModel):
    question: str

@app.post("/chat")
async def chat(body: Ask):
    payload = {
        "model":"llama3.2",
        "prompt":body.question,
        "stream":False
        }
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "http://localhost:11434/api/generate",
            json = payload,
            timeout = 30,
            )
    
    answer = resp.json().get("response", "")
    return {"answer": answer}
    
