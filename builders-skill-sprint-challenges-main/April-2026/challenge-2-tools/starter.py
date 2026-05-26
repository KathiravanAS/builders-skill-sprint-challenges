"""
Challenge 2: Adding Tools to Your Agent
Give your agent a calculator, weather tool, and age calculator.
Model: Amazon Nova Pro via Bedrock
"""

import os
os.environ["BYPASS_TOOL_CONSENT"] = "true"

from datetime import date, datetime
from strands import Agent, tool

from strands.models.ollama import OllamaModel

MODEL = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.2:3b"
)

# ============================================================
# Weather Tool
# ============================================================

@tool
def weather(city: str) -> str:
    """Get the current weather for a city."""
    return f"The weather in {city} is sunny, 28°C"


# ============================================================
# Calculator Tool
# ============================================================

@tool
def calculator(expression: str) -> str:
    """Calculate math expressions."""
    try:
        result = eval(expression)
        return f"The result is {result}"
    except Exception as e:
        return f"Error: {e}"


# ============================================================
# Age Calculator Tool
# ============================================================

@tool
def age_calculator(birth_date: str) -> str:
    """Calculate age from birth date."""

    birth = datetime.strptime(birth_date, "%Y-%m-%d")
    today = date.today()

    age = today.year - birth.year

    if (today.month, today.day) < (birth.month, birth.day):
        age -= 1

    return f"The age is {age} years."


# ============================================================
# Create Agent
# ============================================================

agent = Agent(
    model=MODEL,
    tools=[calculator, weather, age_calculator],
    system_prompt="You are a helpful assistant."
)


# ============================================================
# Test Math
# ============================================================

print("🧮 Math test:")
response = agent("What is 42 * 17?")
print(response)


# ============================================================
# Test Weather
# ============================================================

print("\n🌤️ Weather test:")
response = agent("What's the weather in Chennai?")
print(response)


# ============================================================
# Test Age
# ============================================================

print("\n🎂 Age test:")
response = agent("How old is someone born on 2000-05-15?")
print(response)


print("\n✅ Challenge 2 complete!")