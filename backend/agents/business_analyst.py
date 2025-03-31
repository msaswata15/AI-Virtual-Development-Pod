from crewai import Agent

class BusinessAnalyst:
    def __init__(self):
        self.agent = Agent(
            name="Business Analyst",
            role="Analyzes business requirements and generates user stories.",
            goal="Translate requirements into structured user stories.",
            backstory="Expert in Agile methodologies and requirement analysis.",
            verbose=True
        )
    
    def generate_user_stories(self, requirements):
        return self.agent.think(f"Generate user stories for: {requirements}")
