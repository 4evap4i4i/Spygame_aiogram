from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import Game

router_play = Router()

@router_play.message(Command("play"), Game.started)
async def play(message: Message, state: FSMContext):
    player = {"name": f"{message.from_user.full_name}", "id": f"{message.from_user.id}", "role": None, "votes": 0, "voted": False, "is_started": True}
    player_name = player["name"]

    await state.set_state(Game.players)
    data = await state.update_data(players=[player])
    piski = state.get_data
    await message.answer("Набор в игру начался!\n\n/getin - чтобы вступить в игру (нужно чтобы бот был активирован в личном чате).\n/startgame - чтобы начать игру.")

    await message.answer(f"{player_name} - хост игры!\nТолько он может её начать и закончить!")