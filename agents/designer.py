# agents/designer.py
from crewai import Agent
from utils.llm import LocalLLM
from utils.db import *

class Designer:
    def __init__(self):
        self.llm = LocalLLM()
        self.agent = Agent(
            role="System Designer",
            goal="Create architecture diagrams and update tickets",
            backstory="Software architect with 10+ years experience",
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )
    
    def create_diagram(self, story_id, requirements):
        """Generate design and update ticket"""
        try:
            # Step 1: Generate UML diagram
            prompt = f"""Create Mermaid.js UML diagram for:
            {requirements}
            
            Include:
            - Class diagram
            - Sequence diagram
            - API endpoints
            """
            diagram = self.llm.generate(prompt)
            
            # Step 2: Update ticket
            update_ticket(
                ticket_id=story_id,
                status="Design Completed",
                design=diagram,
            )
            
            return diagram
            
        except Exception as e:
            # Update ticket with error status
            update_ticket(
                ticket_id=story_id,
                status="Design Failed",
                design=f"Error: {str(e)}"
            )
            raise