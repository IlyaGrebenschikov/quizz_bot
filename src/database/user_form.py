from aiogram.fsm.state import State, StatesGroup


class User(StatesGroup):
    level_state = State()
    level_description_state = State()
    gamemode_state = State()
    subscribe_state = State()
    quiz_state = State()
    result_state = State()
    restart_required_state = State()
