import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('.env')

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
# print(OPENAI_API_KEY)
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
# MODEL_NAME = os.getenv("MODEL_NAME", "openai/gpt-5-nano")
# print(f"Using model: {MODEL_NAME}")
# os.environ["HF_TOKEN"] =