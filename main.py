from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
def read_root():
    return Response("WhatsApp Dictionary Chatbot Server is running")