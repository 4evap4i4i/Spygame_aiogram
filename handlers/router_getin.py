from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import Game

router_getin = Router()

@router_getin.message(Command("getin"), Game.players)
async def getin(message: Message, state: FSMContext):
    data = await state.get_value("players")

    player = {"name": f"{message.from_user.full_name}", "id": f"{message.from_user.id}", "role": None, "votes": 0, "voted": False, "is_started": False}
    if player not in data:
        player_fake = player
        player_fake["is_started"] = True
        if player_fake not in data:

            data.append(player)
            player = player["name"]
            await state.update_data(players=data)
            await message.reply(f"{player} - добавлен в игру.")
        else:
            await message.reply("Ты уже в игре!")
    else:
        await message.reply("Ты уже в игре!")