"""
Basic Agent Creation with Strands
Simple demo: Create agent, ask question, get response
"""

import os
from strands import Agent

# Create basic agent with specific model
agent = Agent()

# Ask a question
print("\n💬 Asking: 'What is artificial intelligence?'")

response = agent("What is artificial intelligence?")


# Show different personality
print("\n🎭 Creating agent with custom personality...")

expert_agent = Agent(
    model="us.anthropic.claude-sonnet-4-20250514-v1:0",
    system_prompt="You are a friendly AI expert who explains things simply in Layman terms."
)

response2 = expert_agent("Explain AI in one sentence for a 10-year-old.")
