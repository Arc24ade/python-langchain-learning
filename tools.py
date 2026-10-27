from langchain.tools import tool

@tool
def yo():
     """Prints Rohit."""
     return "Rohit"

res=yo.invoke({})
print(res)