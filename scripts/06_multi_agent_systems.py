#!/usr/bin/env python3
"""
Multi-Agent Systems Demo
Demonstrates swarm-based and graph-based multi-agent coordination
"""

import os
from strands import Agent
from strands_tools import swarm
from strands.multiagent import GraphBuilder

os.environ.setdefault("AWS_REGION", "us-west-2")

print("🤖 MULTI-AGENT SYSTEMS DEMO")

# Swarm coordinator
coordinator = Agent(tools=[swarm])
print("🐝 Swarm analysis:", coordinator("Use 3 agents to analyze AI impact on DevOps jobs"))

# Graph-based workflow with 2 reusable agents
lead = Agent(name="lead", system_prompt="Research leader. Coordinate analysis.")
expert = Agent(name="expert", system_prompt="Domain expert. Provide technical insights.")

builder = GraphBuilder()
builder.add_node(lead, "lead")
builder.add_node(expert, "expert")
builder.add_edge("lead", "expert")
builder.set_entry_point("lead")

result = builder.build()("Evaluate microservices architecture migration")
print(f"🕸️ Graph workflow: {[n.node_id for n in result.execution_order]} - {result.status}")

print("✅ Multi-agent patterns: Swarm + Graph workflows complete!")
