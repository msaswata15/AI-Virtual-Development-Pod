# config.py
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    LLM_MODEL = os.getenv("MODEL_NAME", "llama3")
    KNOWLEDGE_BASE = os.getenv("PERSIST_DIR")