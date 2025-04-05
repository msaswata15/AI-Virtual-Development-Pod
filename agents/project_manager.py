from crewai import Agent
from langchain.llms import HuggingFacePipeline

class ProjectManager:
    def __init__(self):
        self.llm = HuggingFacePipeline.from_pretrained("mistralai/Mistral-7B-Instruct")
        self.agent = Agent(role="Project Manager", model=self.llm)

    def check_progress(self, stage):
        prompt = f"Check the project status for the {stage} phase."
        return self.agent.run(prompt)
