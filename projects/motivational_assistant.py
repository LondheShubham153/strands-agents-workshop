"""
Simple Motivational Chat Assistant
Demo project: Basic Agent + API Tools + Witty Responses
"""

import random
from strands import Agent, tool
from strands_tools import http_request

# Module 1: Building your First AI Agent
class MotivationalAssistant:
    def __init__(self):
        self.agent = Agent(
            model="us.anthropic.claude-sonnet-4-20250514-v1:0",
            system_prompt="""You are a witty, motivational chat assistant. 
            Keep responses short, inspiring, and add humor when appropriate. 
            Always end with an encouraging note.""",
            tools=[self.get_api_quote, self.get_daily_motivation, http_request],
        )
    
    # Module 2: Powering up with Tools
    @tool
    def get_api_quote(self) -> str:
        """Get a motivational quote from free API"""
        try:
            # Using quotable.io - free quotes API
            response = http_request("GET", "https://api.quotable.io/random?tags=motivational")
            if response and 'content' in response and 'author' in response:
                return f"{response['content']} - {response['author']}"
            else:
                return "Every expert was once a beginner. Keep going! 🚀"
        except:
            return "The only way to do great work is to love what you do. - Steve Jobs"
    
    @tool
    def get_daily_motivation(self) -> str:
        """Get daily motivation based on common challenges"""
        motivations = [
            "Feeling stuck? That's just your brain preparing for a breakthrough! 🚀",
            "Every bug you fix makes you stronger. You're basically a code superhero! 💪",
            "Remember: Google exists because even experts need to look things up! 🔍",
            "Your future self is cheering you on right now! Keep going! 🎉",
            "Debugging is like being a detective in a crime movie, except you're both the detective and the criminal! 🕵️"
        ]
        return random.choice(motivations)
    
    def chat(self, message: str) -> str:
        """Simple chat interface"""
        return self.agent(message)

def main():
    """Interactive chat loop"""
    print("🌟 MOTIVATIONAL CHAT ASSISTANT")
    print("Type 'quit' to exit, 'quote' for inspiration, 'motivation' for daily boost!\n")
    
    assistant = MotivationalAssistant()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Assistant: Keep being awesome! See you later! 🌟")
                break
            
            if not user_input:
                continue
            
            response = assistant.chat(user_input)
            print(f"Assistant: {response}\n")
            
        except KeyboardInterrupt:
            print("\nAssistant: Stay motivated! Bye! 👋")
            break
        except Exception as e:
            print(f"Oops! Something went wrong: {e}")

if __name__ == "__main__":
    main()
