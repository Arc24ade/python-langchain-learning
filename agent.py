# The Agent Way (create_agent)

# Best for: When you want to give the model tools (like your get_weather function, calculators, search tools, etc.) so it can autonomously decide when and how to use them.

# code:

from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()


def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    # Your function logic goes here
    return f"The weather in {city} is sunny and 22°C."

# Create an agent with tools and system instructions
agent = create_agent(
    model="google_genai:gemini-3.5-flash-lite",
    tools=[get_weather],  # Your custom Python functions
    system_prompt="You are a helpful assistant",
)

# Invoke it with a message dictionary structure
response = agent.invoke({
    "messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]
})

final_message = response["messages"][-1]
print(final_message.content[0]["text"])