from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states import Game

router_vote = Router()

@router_vote.message(Command("vote"), Game.active)
async def vote(message: Message, state: FSMContext, command: CommandObject):
    data = await state.get_value("active")

    player = next((player for player in data if player.get("name") == f"{message.from_user.full_name}"), None)

    if player is not None:
        if player["voted"] is False:

            player_voted = next((player_voted for player_voted in data if player_voted.get("name") == f"{command.args}"), None)
            if player_voted in data:
                player["voted"] = True
                player_voted["votes"] += 1
                await message.reply("Голос отдан")

            else:
                await message.answer("Такого игрока нет в списке играющих.")
        
        else:
            await message.reply("Ты уже отдал свой голос")
    else:
        await message.answer("Ты не в игре!")

    await state.update_data(active=data)