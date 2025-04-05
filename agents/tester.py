# agents/tester.py
from crewai import Agent
from utils.llm import LocalLLM
from utils.db import update_ticket

class Tester:  # <-- Make sure class name matches
    def __init__(self):
        self.llm = LocalLLM()
        self.agent = Agent(
            role="Quality Assurance Engineer",
            goal="Create and execute test cases",
            backstory="Experienced QA specialist with expertise in automation",
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )
    
    def create_tests(self, story_id, requirements):
        try:
            prompt = f"""Generate test cases for:
            {requirements}
            
            Include:
            - Positive test cases
            - Negative test cases
            - Edge cases"""
            
            tests = self.llm.generate(prompt)
            
            update_ticket(
                ticket_id=story_id,
                status="Testing Completed",
                test_results=tests
            )
            
            return tests
            
        except Exception as e:
            update_ticket(
                ticket_id=story_id,
                status="Testing Failed",
                test_results=f"Error: {str(e)}"
            )
            raise