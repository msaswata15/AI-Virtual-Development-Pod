from crewai import Crew
from utils.llm import LocalLLM
from agents import business_analyst, designer, developer, tester
from crewai import Task  # Import Task from the appropriate module

class DevPod:
    def __init__(self):
        self.llm = LocalLLM()
        
        # Initialize agents with forced verbosity
        self.analyst = business_analyst(self.llm).agent
        self.designer = designer(self.llm).agent
        self.developer = developer(self.llm).agent
        self.tester = tester(self.llm).agent
        
        for agent in [self.analyst, self.designer, self.developer, self.tester]:
            agent.verbose = True

    def run_project(self, requirements):
        print(f"\n🚀 Starting project with requirements:\n{requirements}")
        
        # Create tasks
        analysis_task = Task(
            description=f"Analyze requirements: {requirements}",
            agent=self.analyst,
            expected_output="Detailed user stories in Markdown format",
            async_execution=False  # Force synchronous execution
        )
        
        # Add other tasks...
        
        crew = Crew(
            agents=[self.analyst, self.designer, self.developer, self.tester],
            tasks=[analysis_task],  # Add other tasks
            verbose=2,
            memory=True  # Enable conversation memory
        )
        
        return crew.kickoff(inputs={"requirements": requirements})