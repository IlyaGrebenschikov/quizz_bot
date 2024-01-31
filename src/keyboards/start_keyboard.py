from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton


def start_keyboard() -> ReplyKeyboardMarkup:
    kb = [
            [KeyboardButton(text='/start')]
        ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb)

    return keyboard
