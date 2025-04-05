from crewai import Agent
from utils.llm import LocalLLM
from utils.db import update_ticket
import re

class Developer:
    def __init__(self):
        self.llm = LocalLLM()
        self.agent = Agent(
            role="Senior Software Developer",
            goal="Write clean, efficient, and well-documented code",
            backstory="""10+ years experience in full-stack development.
            Specializes in Python, JavaScript, and API design.
            Follows best practices and clean code principles.""",
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )

    def implement_feature(self, story_id, requirements, design_spec):
        try:
            # Generate code based on requirements and design
            prompt = f"""Write production-ready code for:
            Requirements: {requirements}
            Design Specs: {design_spec}
            
            Guidelines:
            1. Include type hints
            2. Add docstrings
            3. Follow PEP8
            4. Include error handling
            5. Add logging"""
            
            code = self.llm.generate(prompt)
            
            # Clean and validate the code
            clean_code = self._validate_code(code)
            
            # Update ticket in database
            update_ticket(
                ticket_id=story_id,
                status="Development Completed",
                code=clean_code
            )
            
            return clean_code
            
        except Exception as e:
            update_ticket(
                ticket_id=story_id,
                status="Development Failed",
                code=f"Error: {str(e)}"
            )
            raise

    def _validate_code(self, code):
        """Basic code validation and formatting"""
        # Remove markdown code blocks if present
        code = re.sub(r'```[a-z]*\n', '', code)
        code = re.sub(r'\n```', '', code)
        
        # Basic PEP8 validation (would be enhanced with real linter)
        if "import" in code and not code.startswith("import"):
            code = "\n".join(sorted([line for line in code.split("\n") if "import" in line])) + \
                  "\n\n" + \
                  "\n".join([line for line in code.split("\n") if "import" not in line])
        
        return code.strip()