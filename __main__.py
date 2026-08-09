import asyncio
import os

from aiogram import Dispatcher
from aiogram.fsm.strategy import FSMStrategy
from aiohttp import web

from config import Bot
from handlers import routers

dp = Dispatcher(fsm_strategy=FSMStrategy.CHAT)


async def render_naebalovo():
    app = web.Application()
    app.router.add_get("/", lambda r: web.Response(text="ok"))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", int(os.getenv("PORT", 10000)))
    await site.start()

async def main():
    for r in routers:
        dp.include_router(r)

    print("Запуууупукпук")
    await asyncio.gather(render_naebalovo(), dp.start_polling(Bot))

asyncio.run(main())