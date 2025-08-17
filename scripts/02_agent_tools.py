"""
Agent Tools Demo
Simple demo: Create tool, add to agent, use it
"""

import os
import datetime
from strands import Agent, tool
from strands_tools import file_read, shell


# Create a simple tool
@tool
def get_current_time() -> str:
    """Get the current date and time"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Create agent with tools
agent = Agent(
    model="us.anthropic.claude-sonnet-4-20250514-v1:0",
    tools=[get_current_time]
)

# Test the tools
response = agent("What time is it?")


# using in-built tools



agent_with_tools = Agent(
    model="us.anthropic.claude-sonnet-4-20250514-v1:0",
    tools=[file_read,shell]
)

response = agent_with_tools("Can you summarize the file in the path /Users/lshubh/Documents/work/aws/strands-agents/strands-agents-workshop/scripts/02_agent_tools.py?")