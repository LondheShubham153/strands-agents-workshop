"""
Custom Models Demo
Simple demo: Compare different AI models
"""

import os
import time
from strands import Agent
from strands.models import BedrockModel
from strands.models.ollama import OllamaModel



bedrock_model = BedrockModel(
    model_id="us.anthropic.claude-sonnet-4-20250514-v1:0",
    region_name="us-west-2",
    temperature=0.3, # Randomness, (higher number = more random)
)

ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3",
    temperature=0.3, # Randomness, (higher number = more random)
)

bedrock_agent = Agent(model=bedrock_model)
ollama_agent = Agent(model=ollama_model)


question = "Explain quantum computing in one sentence."
print(f"\n💬 Question: {question}")

# Test Bedrock model
print("\n⚡ Bedrock Model (Sonnet 4):")
start = time.time()
bedrock_response = bedrock_agent(question)
bedrock_time = time.time() - start
print(f"\nTime: {bedrock_time:.2f}s")

# Test Ollama model
print("\n🧠 Ollama model (llama 3):")
start = time.time()
ollama_response = ollama_agent(question)
ollama_time = time.time() - start
print(f"\nTime: {ollama_time:.2f}s")

print(f"\n📊 Speed difference: {ollama_time/bedrock_time:.1f}x")



