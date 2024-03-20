import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.methods import DeleteWebhook


logging.basicConfig(level=logging.INFO)


TOKEN = "6939140306:AAHT-TsDEUXn6R9-F5h3Trhe7NNxOUbwZ08"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(f"/start (приветствие и общая информация и информация о командах )\n/registration - Регистрация\n/help")


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())