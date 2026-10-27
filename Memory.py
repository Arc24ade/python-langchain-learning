# conversion History!
from langchain.chat_models import init_chat_model;
import os
from dotenv import load_dotenv

load_dotenv()

llm= init_chat_model(model=os.getenv("MODEL"))

History=[]

while True:
    query= input("user: ")
    if query=="exit":
        break
    
    History.append(query)
    res=llm.invoke(History)
    History.append(res.content[0]['text'])
    print('AI :',res.content[0]['text'])