from aiogram.fsm.state import State, StatesGroup

class Game(StatesGroup):
    started = State()
    players = State()
    active = State()
    end = State()