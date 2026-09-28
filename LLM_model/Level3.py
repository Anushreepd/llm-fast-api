import os

from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

import gradio as gr
load_dotenv()



app = FastAPI()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

class ChatRequest(BaseModel):
    message : str


@app.post("/charts")
def ChartConversation(prompt, history):
    streamData = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role":"system", "content": "You are my ai assiatant"},
            {"role":"user", "content": prompt},
        ],
        temperature = 0.9,
        stream = True
    )
    resp = ""
    for chunck in streamData:
        resp += chunck.choices[0].delta.content or ""
        yield resp

gr.ChatInterface(fn=ChartConversation).launch()
