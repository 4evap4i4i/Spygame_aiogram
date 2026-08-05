import asyncio

from aiogram import Dispatcher
from aiogram.fsm.strategy import FSMStrategy

from config import Bot
from handlers import routers

dp = Dispatcher(fsm_strategy=FSMStrategy.CHAT)

async def main():
    for r in routers:
        dp.include_router(r)

    print("Запуууупукпук")
    await dp.start_polling(Bot)

asyncio.run(main())