"""
Memory-Enabled Agents Demo
Simple demo: Agent remembers conversation context
"""

import os
from strands import Agent
from strands_tools import mem0_memory


# Check if Mem0 API key is available
mem0_key = os.getenv("MEM0_API_KEY")

if mem0_key:
    print("✅ MEM0_API_KEY found - using real memory")
    try:
        agent = Agent(
            model="us.anthropic.claude-sonnet-4-20250514-v1:0",
            tools=[mem0_memory],
        )
        memory_type = "Real Mem0 memory"
    except Exception as e:
        print(f"⚠️ Mem0 error: {e}")
        agent = None
        memory_type = "No memory (Mem0 error)"
else:
    print("⚠️ No MEM0_API_KEY provided")
    agent = None
    memory_type = "No memory (no API key)"

print(f"🔧 Using: {memory_type}")

# Test conversation
if agent:
    print("\n💬 Conversation 1:")
    response1 = agent("Hello Dosto, my name is Shubham and I love DevOps & Cloud.")
    print("\n💬 Conversation 2:")
    response2 = agent("What do you remember about me?")
else:
    print("\n❌ Cannot run conversation - agent not initialized")
