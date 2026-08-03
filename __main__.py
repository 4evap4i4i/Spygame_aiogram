from aiogram import Dispatcher
from config import Bot
from handlers import routers
import asyncio
import pathlib

dp = Dispatcher()

async def main():
    for r in routers:
        dp.include_router(r)

    print("Запуууупукпук")
    await dp.start_polling(Bot)

asyncio.run(main())