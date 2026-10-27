from langchain.agents import create_agent
from langchain.tools import tool
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()
llm= init_chat_model(model=os.getenv("MODEL"))

@tool
def say_name(name):
    """this gives you name of the user"""
    return name

agent = create_agent(
    system_prompt="""
     you are a story teller, based on user request you can tell a story and tell the story in conversational way by adddresing name of the user use say_name tool for that.
    """,

    model=llm,
    tools=[say_name]
)

say_name.invoke({"name":"Rohit"})
query="Tell me a horror story"
res= agent.invoke({"messages":[{"role":"user","content":query}]})
mes=res["messages"][-1].content
print(mes[0]['text'])
