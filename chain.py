
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain.messages import AIMessage

load_dotenv()

llm = init_chat_model(model=os.getenv("MODEL"))

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a five-year-old. Explain things simply."),
    ("human", "{question}")
])

def response(llmres:AIMessage):
    return llmres.content

qna_chain = prompt | llm | response

res = qna_chain.invoke({
    "question": "Explain how a distributed system works."
})

print(res[0]['text'])
