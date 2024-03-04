import asyncio
import os
import logging
import aiohttp

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.filters.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.methods import DeleteWebhook


load_dotenv()
logging.basicConfig(level=logging.INFO)

TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
contact_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Отправить контакт", request_contact=True)]],
                                     resize_keyboard=True)

class RegistrationStates(StatesGroup):
    name = State()
    phone_number = State()
    place = State()
    rate = State()
    location = State()


async def fetch_place_data():

    url = os.environ['API_PLACE']

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data
        

async def send_place(chat_id, options):
    kb = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text=item['name'], callback_data=item['callback_data'])] for item in options]) # one line one item

    await bot.send_message(chat_id, "Выберите район:", reply_markup=kb)


async def fetch_rates_data():

    url = os.environ['API-RATES']

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data
        

async def send_rates(chat_id, options):
    kb = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text=item['name'], callback_data=item['callback_data'])] for item in options], row_width=1)

    await bot.send_message(chat_id, "Выберите тариф:", reply_markup=kb)


async def post_user_info(data):
    url = os.environ['API_ACCOUNT_CREATE']


    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            data = await response.json()
            print(data)
            return data
        

async def user_exist(telegram_id):
    url = f"http://127.0.0.1:8000/account/{telegram_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_code = response.status
            return response_code



@dp.message(CommandStart())
async def start_command(message: types.Message, state: FSMContext):
    await message.answer(f"/start (приветствие и общая информация и информация о командах )\n/registration - Регистрация")


@dp.message(Command("registration"))
async def start_command(message: types.Message, state: FSMContext):
    status = await user_exist(message.from_user.id)
    print(status)
    if status == 404:
        await message.answer(f"Давай начнем процесс регистрации. Введи свое имя:")
        await state.set_state(RegistrationStates.name)
    else:
        await message.answer(f"Вы уже регистрировались!")


@dp.message(RegistrationStates.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text, telegram_id=message.from_user.id)
    await bot.send_message(message.from_user.id, "Отправьте ваш контакт", reply_markup=contact_keyboard)
    await state.set_state(RegistrationStates.phone_number)


@dp.message(RegistrationStates.phone_number, F.contact)
async def process_contact(message: types.Message, state: FSMContext):
    contact = message.contact
    await state.update_data(phone_number=contact.phone_number)

    data = await fetch_place_data()
    
    options = [{'name': item['name'], 'callback_data': str(item['id'])} for item in data]

    await send_place(message.from_user.id, options)

    await state.set_state(RegistrationStates.place)


@dp.callback_query(RegistrationStates.place)
async def callback_query_process_place(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(place=callback_query.data)
    data = await fetch_rates_data()

    options = [{'name': item['rate_name'], 'callback_data': str(item['id'])} for item in data]

    await send_rates(callback_query.from_user.id, options)

    await state.set_state(RegistrationStates.rate)


@dp.callback_query(RegistrationStates.rate)
async def callback_query_process_rate(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(rate=callback_query.data)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[types.KeyboardButton(text="Отправить локацию", request_location=True)]])
    await bot.send_message(callback_query.from_user.id, "Отправьте локацию:", reply_markup=keyboard)
    await state.set_state(RegistrationStates.location)


@dp.message(RegistrationStates.location, F.location)
async def handle_location(message: types.Message, state: FSMContext):
    latitude = message.location.latitude
    longitude = message.location.longitude
    await state.update_data(latitude=latitude, longitude=longitude)
    context = await state.get_data()
    print(context)
    await post_user_info(data=context)

    await bot.send_location(message.from_user.id, latitude=latitude, longitude=longitude)
    
    await bot.send_message(message.from_user.id, "Спасибо за регистрацию!")
    await state.clear()


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
