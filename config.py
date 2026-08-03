from dotenv import load_dotenv
from aiogram import Bot
import os

load_dotenv
Bot = Bot(token=os.getenv("TOKEN"))
db_url = os.getenv("NEON")