from langchain_community.llms import Ollama

class LocalLLM:
    def __init__(self):
        self.llm = Ollama(
            base_url='http://localhost:11434',
            model='llama3',
            temperature=0.3,
            repeat_penalty=1.1
        )
    
    def generate(self, prompt):
        print(f"\n🔵 Sending prompt to LLM:\n{prompt[:200]}...")  # Debug
        response = self.llm.invoke(prompt)
        print(f"\n🟢 Received response:\n{response[:200]}...")
        return response