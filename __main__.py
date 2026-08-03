from aiogram import Dispatcher
from config import Bot
from handlers import routers
import aiosqlite
import asyncio
import pathlib

base = pathlib.Path("roles.db")
async def create():
    async with aiosqlite.connect("roles.db") as db:
        await db.execute(
        """
        CREATE TABLE roles (
            Id INTEGER PRIMARY KEY,
            Role TEXT
        );
        """
        )

if not base.exists():
    asyncio.run(create())

dp = Dispatcher()

async def main():
    for r in routers:
        dp.include_router(r)

    print("piski siski")
    await dp.start_polling(Bot)

asyncio.run(main())