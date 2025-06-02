

# Importing necessary classes and functions from openai-agents SDK
from agents import Agent, Runner, function_tool
from agents.extensions.models.litellm_model import LitellmModel


GEMINI_API_KEY = "YOUR_GOOGLE_GEMINI_API_KEY"

# Model to use
MODEL = 'gemini/gemini-2.0-flash'

# A simple function tool that pretends to get weather info for a city
@function_tool
def get_weather(city: str) -> str:
    print(f"[debug] getting weather for {city}")
    return f"The weather in {city} is sunny."

# Creating an AI agent with a name and instructions
# This agent will respond only in haiku format
agent = Agent(
    name="Assistant",
    instructions="You only respond in haikus.",
    model=LitellmModel(model=MODEL, api_key=GEMINI_API_KEY),
)

# Run the agent synchronously with a question
result = Runner.run_sync(agent, "What's the weather in Tokyo?")

# Printing the agent's final haiku response
print(result.final_output)
