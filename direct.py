from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
model=os.getenv("MODEL")
api_key=os.getenv("GOOGLE_API_KEY")

geminillm= ChatGoogleGenerativeAI(model=model,api_key=api_key)

res= geminillm.invoke("write essay on cow")
print(res.content[0]['text'])





