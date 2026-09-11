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

@app.get("/chats")
def chatData():
    return "Welcome to chat bot"


@app.post("/chats")
def chartData(prompt: ChatRequest):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": "Your a my assisstant"},
            {"role": "user", "content": prompt.message},
        ],
        temperature= 0.9,
        stream = True
    )
    return response.choices[0].message.content

@app.post("/chats_gradio")
def chatGradio(message):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "user", "content": message}
        ],
        temperature= 0.9,
    )
    return response.choices[0].message.content

gr.Interface(fn = chatGradio, inputs = "text", outputs = "text").launch()
