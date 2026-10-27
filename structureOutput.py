from pydantic import BaseModel,Field
from langchain.chat_models import init_chat_model;
import os
from dotenv import load_dotenv

load_dotenv()

llm= init_chat_model(model=os.getenv("MODEL"))


class User(BaseModel):
    name:str=Field(description="write your full name!")
    age:int=Field(description="write your age in Interger!")
    email:str=Field(description="Write you email address!")

llm_with_stu_out=llm.with_structured_output(User)

res= llm_with_stu_out.invoke("hello, my name is Rohit pandey age 22 and email= rohitpaney3946@gamil.com")

print(res.model_dump())

