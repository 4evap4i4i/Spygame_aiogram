import os

from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()
Bot = Bot(token=os.getenv("TOKEN"))
db_url = os.getenv("NEON")