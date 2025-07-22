from dotenv import load_dotenv
import os

load_dotenv()  # get api keys from .env

LLM_API = os.getenv("LLM_API")
BOT_API = os.getenv("TELEGRAMM_BOT_API")