"""
Advanced Example: Code Review Agent
Simple demo: Agent reviews code and provides feedback
"""

import os
from strands import Agent, tool
from strands_tools import file_read, shell

# Configure environment
os.environ.setdefault("AWS_REGION", "us-west-2")

print("👨‍💻 Creating a code review agent...")

@tool
def analyze_code(code: str) -> str:
    """Analyze code for basic metrics"""
    lines = len([l for l in code.split('\n') if l.strip()])
    functions = code.count('def ')
    classes = code.count('class ')
    complexity = "Low" if lines < 10 else "Medium" if lines < 50 else "High"
    
    return f"Analysis: {lines} lines, {functions} functions, {classes} classes, {complexity} complexity"

@tool
def check_style(code: str) -> str:
    """Check basic Python style"""
    issues = []
    if '\t' in code:
        issues.append("Uses tabs instead of spaces")
    if any(len(line) > 100 for line in code.split('\n')):
        issues.append("Lines too long (>100 chars)")
    
    return f"Style issues: {', '.join(issues) if issues else 'None found'}"

# Create specialized agent
agent = Agent(
    model="us.anthropic.claude-sonnet-4-20250514-v1:0",
    tools=[analyze_code, check_style, file_read, shell],
    system_prompt="You are a senior code reviewer. Analyze code and provide constructive feedback."
)

# Sample code to review
sample_code = """
def calculate_total(items):
    total = 0
    for item in items:
        if item.get('price', 0) > 0:
            total += item['price'] * item.get('quantity', 1)
    return total

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        self.items.append({'name': name, 'price': price, 'quantity': quantity})
"""

print(f"\n📝 Code to review:\n{sample_code}")

print("\n💬 Asking agent to review the code...")
response = agent(f"Please review this Python code and provide feedback:\n{sample_code}")

# Create new specialized agent
agent = Agent(
    model="us.anthropic.claude-sonnet-4-20250514-v1:0",
    tools=[file_read, shell],
    system_prompt="You are a senior code reviewer with all the special tools for reading files.\
         Analyze code and provide constructive feedback."
)

response = agent(f"Please review code from file /Users/lshubh/Documents/work/aws/strands-agents/strands-agents-workshop/scripts/04_memory_agents.py and provide feedback:\n{sample_code}")
