import json
from pathlib import Path
from mcp import stdio_client, StdioServerParameters
from strands import Agent
from strands.models import BedrockModel
from strands.tools.mcp import MCPClient

class AWSDocsAgent:
    """AWSDocs Agent with MCP integration for Better Docs Summary"""
    
    def __init__(self):
        self.mcp_client = self._create_mcp_client()
        self.model = self._create_model()
        self.system_prompt = self._get_system_prompt()
    
    def _load_mcp_config(self) -> dict:
        mcp_config_path = Path.cwd() / "mcp.json"
        
        with open(mcp_config_path, 'r') as f:
            config = json.load(f)
        
        return config["mcpServers"]["awslabs.aws-documentation-mcp-server"]
    
    def _create_mcp_client(self) -> MCPClient:
        """Create AWS Documentation client using stdio transport"""
        aws_docs_config = self._load_mcp_config()
        
        return MCPClient(lambda: stdio_client(
            StdioServerParameters(
                command=aws_docs_config["command"],
                args=aws_docs_config["args"],
                env=aws_docs_config.get("env", {})
            )
        ))
    
    def _create_model(self) -> BedrockModel:
        """Create Bedrock model for the agent"""
        return BedrockModel(
            model_id="us.anthropic.claude-sonnet-4-20250514-v1:0",
            region_name="us-west-2",
            temperature=0.3,
        )
    
    def _get_system_prompt(self) -> str:
        """Get system prompt for AWS Documentation operations"""
        return """You are a AWS Documentation summary expert assistant. You can help with:
- Querying AWS Docs with plain english
- Summarizing Long documentations with important things for the Developers, cloud Engineers  

Keep responses concise and short."""
    
    def query(self, user_input: str) -> str:
        """Process user query with AWS Docs MCP tools"""
        with self.mcp_client:
            tools = self.mcp_client.list_tools_sync()
            
            agent = Agent(
                model=self.model,
                system_prompt=self.system_prompt,
                tools=tools
            )
            
            return agent(user_input)

def main():
    docs_agent = AWSDocsAgent()
    
    print("AWS Docs Agent Ready! Type 'quit' to exit.")
    print("-" * 40)
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Bye from AWS Docs Agent!")
                break
            
            if not user_input:
                continue
            
            print("\nAgent:", end=" ")
            response = docs_agent.query(user_input)
            print(response)
            
        except KeyboardInterrupt:
            print("\nBye from AWS Docs Agent!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
