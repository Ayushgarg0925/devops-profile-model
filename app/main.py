from fastapi import FastAPI
from pydantic import BaseModel
from app.config import load_config
from app.model import load_model, generate_text

app = FastAPI()

config = load_config()
model, tokenizer = load_model(config)


class Request(BaseModel):
    prompt: str


@app.get("/")
def health():
    return {"status": "ok", "profile": config}


@app.post("/generate")
def generate(req: Request):
    output = generate_text(
        model,
        tokenizer,
        req.prompt,
        config.get("max_tokens", 50)
    )
    return {"response": output}