from fastapi import FastAPI, Form, Response, HTTPException
import requests
from utils import send_message
from dotenv import load_dotenv
import os
from model import dictionary_collection

load_dotenv()

app = FastAPI()
whatsapp_number = os.getenv("TO_NUMBER")
api_key = os.getenv("DICTIONARY_API_KEY")

@app.get("/")
def read_root():
    return Response(content="WhatsApp Dictionary Chatbot Server is running")

@app.post("/message")
async def reply(Body: str = Form()):
    if not Body.isalpha():
        flag = "Please give a valid word"
        send_message(whatsapp_number, flag)
        return Response(content=flag, status_code=400)
    
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{Body}?key={api_key}"
    response = requests.get(url)
    
    if response.status_code != 200:
        error_message = "Error contacting dictionary API"
        send_message(whatsapp_number, error_message)
        raise HTTPException(status_code=response.status_code, detail=error_message)
    
    data = response.json()
    
    if not data or 'shortdef' not in data[0]:
        not_found_message = "No definition found"
        send_message(whatsapp_number, not_found_message)
        return Response(content=not_found_message, status_code=404)
    
    definition = data[0]["shortdef"][0]
    send_message(whatsapp_number, definition)
    
    dictionary_db = {"word": Body, "definition": definition}
    dictionary_collection.insert_one(dictionary_db)
    
    return {"word": Body, "definition": definition}
