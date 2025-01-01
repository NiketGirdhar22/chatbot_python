# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from chatbot.chatbot import SentimentChatBot

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class Message(BaseModel):
#     text: str

# class Response(BaseModel):
#     reply: str 

# sentiment_file = './data/sentiment_data.json' 
# responses_file = './data/responses.json'  
# chatbot = SentimentChatBot(sentiment_file, responses_file)

# @app.post("/chat", response_model=Response)
# def chat(message: Message):
#     try:
#         reply = chatbot.chat(message.text)
#         return {"reply": reply}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Sentiment ChatBot API!"}


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chatbot.chatbot import SentimentChatBot

app = FastAPI()

class MessageRequest(BaseModel):
    message: str

@app.post("/chat/")
async def chat_with_bot(request: MessageRequest):
    sentiment_file = './data/sentiment_data.json'
    responses_file = './data/responses.json'
    
    # Initialize the chatbot
    chatbot = SentimentChatBot(sentiment_file, responses_file)
    
    # Call the chat method with the message
    response = chatbot.chat(request.message)
    
    # Return the chatbot's response
    return {"response": response}
