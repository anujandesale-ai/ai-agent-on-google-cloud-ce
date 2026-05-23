import os
from dotenv import load_dotenv
load_dotenv()
print(f"Key loaded: {'Yes' if os.getenv('OPENAI_API_KEY') else 'No'}")
