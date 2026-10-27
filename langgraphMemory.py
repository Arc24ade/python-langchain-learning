from langgraph.checkpoint.memory import InMemorySaver
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

load_dotenv()
llm= init_chat_model(model=os.getenv("MODEL"))


agent = create_agent(
    system_prompt="""
     help me to do maths
     
    """,
    model=llm,
    checkpointer=InMemorySaver()
)

while True:
    query= input("user: ")
    if query =="exit":
        break
    
    res= agent.invoke({"messages":[{"role":"user","content":query}]},
    {"configurable":{"thread_id":"user_1"}}
    )
    mes=res["messages"][-1].content
    print("AI: ",mes[0]['text'])