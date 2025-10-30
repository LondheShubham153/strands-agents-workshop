from typing import Dict, List, Any
import json
import time
from enum import Enum
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent
from strands_tools import http_request

app = BedrockAgentCoreApp()

class AgentRole(Enum):
    PLANNER = "planner"
    RETRIEVER = "retriever"
    ANALYST = "analyst"
    VALIDATOR = "validator"

class MultiAgentSystem:
    def __init__(self):
        self.agents = {
            AgentRole.PLANNER: Agent(
                system_prompt="Break complex problems into 2-3 actionable subtasks. "
                             "Provide clear, structured response."
            ),
            AgentRole.RETRIEVER: Agent(
                system_prompt="Identify relevant information sources and key data points. "
                             "Provide structured information summary.",
                tools=[http_request]
            ),
            AgentRole.ANALYST: Agent(
                system_prompt="Provide expert analysis and actionable insights. "
                             "Give clear findings and recommendations."
            ),
            AgentRole.VALIDATOR: Agent(
                system_prompt="Validate analysis quality, accuracy, and completeness. "
                             "Provide validation status and quality assessment."
            )
        }
        self.execution_trace = []
    
    def execute_agent(self, role: AgentRole, prompt: str) -> Dict[str, Any]:
        start_time = time.time()
        
        try:
            agent = self.agents[role]
            response = agent(prompt)
            
            # Simple response extraction
            response_text = str(response)
            if hasattr(response, 'message'):
                response_text = response.message
            
            output = {"content": response_text, "status": "success"}
            confidence = 0.9
            
        except Exception as error:
            output = {"error": str(error), "status": "failed"}
            confidence = 0.2
        
        execution_time = time.time() - start_time
        
        return {
            "role": role.value,
            "output": output,
            "confidence": confidence,
            "execution_time": execution_time
        }
    
    def process_query(self, user_query: str) -> Dict[str, Any]:
        pipeline_start = time.time()
        self.execution_trace = []
        
        # Execute agents in sequence
        agents_sequence = [
            (AgentRole.PLANNER, f"Analyze and break down this request: {user_query}"),
            (AgentRole.RETRIEVER, f"Identify key information sources for: {user_query}"),
            (AgentRole.ANALYST, f"Provide expert analysis for: {user_query}"),
            (AgentRole.VALIDATOR, f"Validate the analysis quality for: {user_query}")
        ]
        
        for role, prompt in agents_sequence:
            result = self.execute_agent(role, prompt)
            self.execution_trace.append(result)
        
        # Calculate metrics
        total_time = time.time() - pipeline_start
        avg_confidence = sum(step["confidence"] for step in self.execution_trace) / len(self.execution_trace)
        
        # Build response
        return {
            "query": user_query,
            "status": "success" if avg_confidence > 0.6 else "needs_review",
            "execution_trace": [
                {
                    "step": idx + 1,
                    "agent": step["role"],
                    "confidence": f"{step['confidence']:.1%}",
                    "execution_time": f"{step['execution_time']:.2f}s",
                    "output": step["output"]
                }
                for idx, step in enumerate(self.execution_trace)
            ],
            "summary": {
                "total_execution_time": f"{total_time:.2f}s",
                "average_confidence": f"{avg_confidence:.1%}",
                "agents_executed": len(self.execution_trace)
            },
            "results": {
                "confidence_level": "high" if avg_confidence > 0.8 else "medium" if avg_confidence > 0.6 else "low"
            }
        }

multi_agent_system = MultiAgentSystem()

@app.entrypoint
def invoke(payload: Dict[str, Any]) -> Dict[str, Any]:
    user_query = payload.get("prompt", "Hello! How can I help you today?")
    
    print(f"\n Processing Query: {user_query}")
    print("=" * 60)
    
    try:
        result = multi_agent_system.process_query(user_query)
        
        print(f"Status: {result['status']}")
        print(f"Time: {result['summary']['total_execution_time']}")
        print(f"Confidence: {result['summary']['average_confidence']}")
        
        return result
        
    except Exception as error:
        print(f"Error: {str(error)}")
        return {
            "query": user_query,
            "status": "error",
            "error_message": str(error)
        }

if __name__ == "__main__":
    print("Multi-Agent Chain of Thought System")
    print("Starting server on http://0.0.0.0:8080")
    app.run(host="0.0.0.0", port=8080)
