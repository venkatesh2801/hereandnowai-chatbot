from openai import OpenAI
from dotenv import load_dotenv
import os 
import PyPDF2

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
model = "gemini-2.5-flash-lite"
base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"




