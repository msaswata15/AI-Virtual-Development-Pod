from crewai import Agent

class DeveloperAgent:
    def __init__(self):
        self.agent = Agent(
            name="Developer",
            role="Writes code based on user stories.",
            goal="Generate Python/JavaScript code snippets.",
            backstory="Experienced software developer.",
            verbose=True
        )
    
    def write_code(self, user_story):
        return self.agent.think(f"Write code for: {user_story}")
