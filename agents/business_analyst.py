# agents/business_analyst.py
from crewai import Agent
from utils.llm import LocalLLM
from utils.db import create_ticket
from utils.llm import LocalLLM  # Instead of local_llm
class BusinessAnalyst:
    def __init__(self):
        self.llm = LocalLLM()
        self.agent = Agent(
            role="Business Analyst",
            goal="Create user stories",
            backstory="Expert in Agile methodologies",
            tools=[self.create_story],
            llm=self.llm
        )
    
    def create_story(self, requirements):
        prompt = f"Convert to user story:\n{requirements}\nFormat: 'As a [role], I want [feature] so that [benefit]'"
        story = self.llm.generate(prompt)
        create_ticket(story.split('\n')[0], story)
        return story