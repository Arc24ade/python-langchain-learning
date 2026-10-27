from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(model=os.getenv("MODEL"))

prompt=ChatPromptTemplate.from_messages([
    {"role":"system","content":"You are 7 years {language} developer!"},
    {"role":"user","content":"{query}"}
    
])

res=prompt.invoke({"language":"java","query":"write print hello code!"})

resp=llm.invoke(res)

print(resp.content[0]['text'])
