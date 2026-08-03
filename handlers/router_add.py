from aiogram import Router
from states import Game
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
import aiosqlite

router_add = Router()

@router_add.message(Command("add"))
async def add(message: Message, command: CommandObject):
    if message.chat.type == "private":
        if command.args is not None:

            async with aiosqlite.connect("roles.db") as db:
                async with db.execute("SELECT role FROM roles WHERE role == ?;", (command.args,)) as cursor:
                    row = await cursor.fetchone()

                    if row is not None:
                        await message.reply("Такая роль уже есть.")
                    
                    else:
                        async with aiosqlite.connect("roles.db") as db:
                            await db.execute("INSERT INTO roles (role) VALUES (?)", (command.args,))
                            await db.commit()
                        
                        await message.reply("Роль добавлена!")
        else:
            await message.reply("Напиши хоть чото")     
    else:
        await message.reply("Добавлять роли можно только в личном чате!")