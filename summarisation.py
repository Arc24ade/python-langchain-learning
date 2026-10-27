
from langgraph.checkpoint.memory import InMemorySaver
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware

load_dotenv()

llm = init_chat_model(model=os.getenv("MODEL"))

chat = [
    "My name is Rohit.",
    "I am learning Python.",
    "Python is easy to learn.",
    "I want to become a software developer.",
    "I practice coding every day.",
    "I enjoy solving programming problems.",
    "I am learning artificial intelligence.",
    "Machine learning is an interesting field.",
    "I want to build my own projects.",
    "I use VS Code for programming.",
    "Python supports object-oriented programming.",
    "A function is a reusable block of code.",
    "Lists are mutable in Python.",
    "A dictionary stores key-value pairs.",
    "A tuple is immutable.",
    "I am learning data structures and algorithms.",
    "Consistency is the key to success.",
    "I want to improve my problem-solving skills.",
    "Programming requires patience and practice.",
    "I will never stop learning new things.",
    "Today I learned something new.",
    "I am working on a Python project.",
    "Debugging helps me find errors in my code.",
    "I want to understand how large language models work.",
    "Generative AI is changing the world."
]

agent = create_agent(
    model=llm,
    system_prompt="You are a helpful assistant who answers questions about Python and programming.",
    checkpointer=InMemorySaver(),
    middleware=[
        SummarizationMiddleware(
            model=llm,
            trigger=("messages", 6),
            keep=("messages", 2)
        )
    ]
)

config = {
    "configurable": {
        "thread_id": "user_1"
    }
}

for msg in chat:
    agent.invoke(
        {"messages": [{"role": "user", "content": msg}]},
        config=config
    )

    print("Messages in History: ",len(agent.get_state(config).values["messages"]))
