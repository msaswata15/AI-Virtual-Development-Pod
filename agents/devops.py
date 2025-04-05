from crewai import Agent
from utils.llm import LocalLLM
from utils.ci_cd import trigger_pipeline

class DevOps:
    def __init__(self):
        self.llm = LocalLLM()
        self.agent = Agent(
            role="DevOps Engineer",
            goal="Automate deployments and infrastructure",
            backstory="Cloud and CI/CD specialist",
            tools=[self.deploy],
            llm=self.llm
        )
    
    def deploy(self, version):
        prompt = f"Create deployment plan for version {version}"
        plan = self.llm.generate(prompt)
        trigger_pipeline(version)
        return f"Deployed {version}\nPlan:\n{plan}"