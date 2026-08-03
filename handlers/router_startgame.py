from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import Game
from config import Bot
from random import shuffle
from config import db_url
import asyncpg

router_startgame = Router()

@router_startgame.message(Command("startgame"), Game.players)
async def startgame(message: Message, state: FSMContext):
    data = await state.get_value("players")

    player_sender = next((player for player in data if player.get("name") == f"{message.from_user.full_name}"), None)

    if player_sender["is_started"] is True:
        db = await asyncpg.connect(db_url)
        row = await db.fetchrow("""
            SELECT role
            FROM roles
            ORDER BY id
            LIMIT 1
            OFFSET floor(random() * (SELECT COUNT(*) FROM roles))::int
        """)

        shuffle(data)

        for player in data:
            player["role"] = row[0]
        
        data[-1]["role"] = "щпион"

        for player in data:
            try:
                piska = player["role"]

                await Bot.send_message(chat_id=player["id"], text=f"Твоя роль - {piska}")

            except Exception:
                player_bad = player["name"]
                await message.answer(f"У игрока {player_bad} бот не запущен, он не будет участвовать в игре.")

                data.remove(player)
                print(data)
        
        if data:
            await state.set_state(Game.active)
            await state.update_data(active=data)

            shuffle(data)
            players_query = ""
            for player in data:
                players_query += player["name"] + " "

            await message.answer(f"Игра началась!\n\nПусть очередь ответов будет такой: {players_query}\n\nОбсуждать игру можно свободно, да и очередь - случайный порядок игроков, ей можно не следовать.\nКороче делайте чо хотите\n\n/vote 'ник игрока в чате(не юз)' - чтобы отдать голос за другого игрока\n/end - для окончания игры (работает только у того, кто начал игру через /play)")
        else:
            await state.set_state(Game.started)
            await message.answer('Нет игроков, игра отменена!')

    else:
        await message.reply("Ты не в игре!")