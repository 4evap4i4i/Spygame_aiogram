from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router_help = Router()

@router_help.message(Command("help"))
async def help(message: Message):
    await message.answer('Список комманд и их описание:\n\n/start - для активации бота.\n/play - для начала набора в игру. Игрок написавший эту команду станет хостом.\n/getin - команда, чтобы принять участие в игре.\n/startgame - начать игру (сработает только у хоста).\n/vote - отдать голос за другого игрока (/vote "ник игрока").\n/end - закончить игру (работает только у хоста).\n/cancel - отмена игры и любых других действий.\n/add - для добавления роли (добавится во все игры, даже других игроков, работает только в личном чате)\n\n/donate + кол-во звёзд - закинуть донат разрабам (только в лс)')