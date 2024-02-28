import asyncio
import os
import logging
import aiohttp

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command

load_dotenv()
logging.basicConfig(level=logging.INFO)

TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


async def fetch_rates_data():

    url = "http://127.0.0.1:8000/rates"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data
        

async def send_rates(chat_id, options):
    kb = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text=item['name'], callback_data=item['callback_data'])] for item in options])

    await bot.send_message(chat_id, "Rates:", reply_markup=kb)


@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(f"Hi {message.from_user.first_name}.")


@dp.message(Command("rates"))
async def rates_command(message: types.Message):
    data = await fetch_rates_data()

    options = [{'name': item['rate_name'], 'callback_data': str(item['id'])} for item in data]

    await send_rates(message.from_user.id, options)



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
