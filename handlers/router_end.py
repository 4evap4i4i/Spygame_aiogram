from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from states import Game
from config import Bot
from random import choice
import asyncio

router_end = Router()

@router_end.message(Command("end"), Game.active)
async def end(message: Message, state: FSMContext):

    data = await state.get_value("active")

    player_sender = next((player for player in data if player.get("name") == f"{message.from_user.full_name}"), None)

    if player_sender["is_started"] is True:
        player_high = data[0]
        player_many = []

        for player in data:
            if player_high["votes"] > player["votes"]:
                player_high = player
                print(player_high)
            elif player_high["votes"] < player["votes"]:
                print(player_high)

        player_highscore_name = player_high["name"]
        player_highscore_role = player_high["role"]
        msg = await message.answer(f"{player_highscore_name} - игрок с самым большим количеством голосов и")
        msg_text = msg.text

        await asyncio.sleep(0.33)
        await msg.edit_text(text=(msg_text + "..."))

        for _ in range(3):
            await asyncio.sleep(0.33)
            msg_text += "."
            await msg.edit_text(text=msg_text)
            
        await message.answer(f"{player_highscore_name} - {player_highscore_role}")

        await state.set_state(Game.started)
    else:
        await message.reply("дабляяяяяяя как же ты заебал сын фермера вонючий иди нахуй ххватить руинить пидарасина ибучая ишак ипаный")

    return