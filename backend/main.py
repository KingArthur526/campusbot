from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ollama
from .rag import need_context

app = FastAPI()

@app.get("/ping")
def ping():
    return {"Shraddha":"sleeping"}

class Ask(BaseModel):
    question: str

@app.post("/chat")
async def chat(body: Ask):
    client = ollama.Client("http://localhost:11434")

    context = need_context(body.question)
    
    prompt = f"""Context: {context} Question:{body.question}"""

    reply = client.chat(
        model = "llama3.2",
        messages = [{"role": "user", "content":prompt}],
        stream = False
        )
    
    return {"Answer": reply["message"]["content"]}
