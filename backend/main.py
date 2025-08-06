from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ollama
import httpx

app = FastAPI()

@app.get("/ping")
def ping():
    return {"Shraddha":"sleeping"}

class Ask(BaseModel):
    question: str

@app.post("/chat")
async def chat(body: Ask):
    client = ollama.Client("http://localhost:11434")
    
    prompt = f"""Context: {"Shraddha is a college girl. She is extremely adventurous and meets a talking dog on the way to college one day"} Question:{body.question}"""

    response = client.generate(
        model = "llama3.2",
        prompt=prompt
    )
    
    return {"Answer": response.response}
