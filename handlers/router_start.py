from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from states import Game

router_start = Router()

@router_start.message(CommandStart())
async def start(message: Message, state: FSMContext):
    if message.chat.type == "private":
        try:
            await message.answer_animation(caption="Привет! Это бот для игры в шпиона!\n\nК сожалению он работает только в групповом чате.\nИ тебе придётся пообщаться с другими людьми чтобы поиграть.\n\nЕщё можно выйти на улицу и потрогать траву (опционально)\n\nЗато ты можешь прописать /help чтобы увидеть весь список команд бота\n\nЗато ты можешь прописать команду /add чтобы добавить роль в игру.\n\nА также /donate + циферка - чтобы поддержать бота.", animation="https://c.tenor.com/QqVL1Ogea6cAAAAC/tenor.gif")
        except Exception:
            await message.answer("Привет! Это бот для игры в шпиона!\n\nК сожалению он работает только в групповом чате.\nИ тебе придётся пообщаться с другими людьми чтобы поиграть.\n\nЕщё можно выйти на улицу и потрогать траву (опционально)\n/help - для полного списка команд.")

    elif message.chat.type == "group":
        await state.set_state(Game.started)
        try:
            await message.answer_animation(caption="Привет, это бот для игры в шпиона!\n\nЧтобы начать игру - кто-нибудь должен прописать команду /play\n\nЧтобы отменить текущую игру - кто-нибудь должен прописать команду /cancel\n/help - для полного списка команд.", animation="https://c.tenor.com/ojjiAPMVYwMAAAAd/tenor.gif'")
        except Exception:
            await message.answer("Привет, это бот для игры в шпиона!\n\nЧтобы начать игру - кто-нибудь должен прописать команду /play\n\nЧтобы отменить текущую игру - кто-нибудь должен прописать команду /cancel\n/help - для полного списка команд.")