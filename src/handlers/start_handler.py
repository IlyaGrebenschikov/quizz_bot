from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram import Router

from src.keyboards import start_keyboard


router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    keyboard = start_keyboard()
    await message.answer(f'ЗДАРОВА, {hbold(message.from_user.full_name)}!', reply_markup=keyboard)
