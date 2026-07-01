import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Read API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Model Name
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")

# Create model object
model = genai.GenerativeModel(MODEL_NAME)