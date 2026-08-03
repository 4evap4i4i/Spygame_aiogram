from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from states import Game

router_cancel = Router()

@router_cancel.message(Command("cancel"))
@router_cancel.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.set_state(Game.started)
    await message.answer("Игра отменена.")