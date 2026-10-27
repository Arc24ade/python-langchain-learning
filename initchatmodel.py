import os
from dotenv import load_dotenv
from langchain.messages import SystemMessage,HumanMessage
from langchain.chat_models import init_chat_model


load_dotenv()
llm=init_chat_model(model=os.getenv("MODEL"))
# res=llm.invoke([
#     {'role':'system','content':"you are a infact baby you can't even talk."},
#     {"role":"user","content":"how are you??"}
# ])
# print(res.content[0]['text'])


prompts=[
    SystemMessage(content="you are a five year old."),
    HumanMessage(content="Explain me who distributed system works")
]

res=llm.invoke(prompts)
print(res.content[0]['text'])
