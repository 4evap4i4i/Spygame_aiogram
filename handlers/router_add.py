from aiogram import Router
from states import Game
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from config import db_url
import asyncpg

router_add = Router()

@router_add.message(Command("add"))
async def add(message: Message, command: CommandObject):
    if message.chat.type == "private":
        if command.args is not None:
            
            try:
                db = await asyncpg.connect(db_url)
                row = await db.fetchrow("SELECT role FROM roles WHERE role = $1", command.args)
                print(command.args)

                if row is not None:
                    await message.reply("Такая роль уже есть.")
                    await db.close()
                    print(row)
                else:
                    await db.execute("INSERT INTO roles (role) VALUES ($1)", command.args)
                    await db.close()
                    
                    await message.reply("Роль добавлена!")

            except Exception as e:
                print(e)
                await message.answer(f"Извини, таблица ролей переполнена.{e}")
        else:
            await message.reply("Напиши хоть что-то")     
    else:
        await message.reply("Добавлять роли можно только в личном чате!")