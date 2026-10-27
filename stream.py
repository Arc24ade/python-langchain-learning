
from langchain.chat_models import init_chat_model;
import os
from dotenv import load_dotenv

load_dotenv()

llm= init_chat_model(model=os.getenv("MODEL"),streaming=True)

res= llm.stream('Explain ml in 500 words')

for chunk in res:
    print(chunk.content[0]['text'],end='',flush=True)


