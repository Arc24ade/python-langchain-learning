
from langgraph.checkpoint.memory import InMemorySaver
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware,PIIMiddleware

load_dotenv()

llm = init_chat_model(model=os.getenv("MODEL"))



agent = create_agent(
    model=llm,
    system_prompt="You are a helpful assistant who answers questions about Python and programming.",
   
    middleware=[
        PIIMiddleware("email",strategy="redact",apply_to_input=True),
        PIIMiddleware("credit_card",strategy="mask",apply_to_input=True)
    ]
)

query="hello i received  payment from email rohitpandey3946@gmail.com credit card 5105-1051-0510-5100."
res=agent.invoke({
    "messages":[{"role":"user","content":query}]
})

print(res['messages'][0].content)