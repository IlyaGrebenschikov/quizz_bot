import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from src.core import get_settings
from src.handlers import start_router


async def main() -> None:
    token = get_settings().token.get_token
    dp = Dispatcher()
    bot = Bot(
        token=token,
        parse_mode=ParseMode.HTML
    )

    dp.include_router(start_router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
