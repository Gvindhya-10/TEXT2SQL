import psycopg2
from dotenv import load_dotenv
import os

# Right after loading the environment variables in api.py
load_dotenv()

gemini_api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")

# Add these print statements to check if the variables are loaded correctly
print(f"GEMINI API Key: {gemini_api_key}")
print(f"Database URL: {database_url}")

if gemini_api_key is None:
    raise ValueError("API_KEY not found in environment variables")

