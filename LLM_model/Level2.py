import os

from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv

import gradio as gr

load_dotenv()
app = FastAPI()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

class ChatRequest(BaseModel):
    message : str

@app.post("/chats_gradio")
def chatGradio(message, history):
    stream = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "user", "content": message}
        ],
        temperature= 0.9,
        stream = True
    )
    result = ""
    for chunks in stream:
        result += chunks.choices[0].delta.content or ""
        yield result
    

gr.ChatInterface(fn = chatGradio).launch()
