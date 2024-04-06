import asyncio
import os
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.methods import DeleteWebhook
from states.states import RegistrationStates, ProfileState, DefaultState
from fetches.fetch import fetch_place_data, fetch_rates_data, post_user_info, user_exist, get_user_data, delete_user_data, user_change_column
from keyboards.keyboard import contact_keyboard, confirm_keyboard, delete_keyboard, register_keyboard, location_keyboard, profile_view_keyboard, profile_column_keyboard


load_dotenv()
logging.basicConfig(level=logging.INFO)

TOKEN = os.environ['WORKER-TOKEN']
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


async def send_place(message, options):
    kb = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text=item['name'], callback_data=item['callback_data'])] for item in options]) # one line button one item 

    await bot.send_message(message.from_user.id, "Выберите район:", reply_markup=kb)


@dp.message(CommandStart())
async def start_command(message: types.Message, state: FSMContext):
    user_data = await get_user_data(message.from_user.id, token=TOKEN)
    if user_data != None:
        await message.answer("""
Для пользования бота можете использовать следующие комманды:

/start - Для начала использования или для рестарта
/help - Для помощи
                             
Нажмите на кнопку - Профиль - для полной информации вашего аккаунта
                             """, reply_markup=profile_view_keyboard)
    else:
        await message.answer(f"""
Для пользования бота можете использовать следующие комманды:

/start - Для начала использования или для рестарта
/help - Для помощи
                             
Что бы пройти регистрацию нажмите на кнопку
                             """, reply_markup=register_keyboard)


@dp.message(RegistrationStates.name)
async def process_name(message: types.Message, state: FSMContext):
    try:
        full_name = message.text.split(" ")
        await state.update_data(first_name=full_name[0], last_name=full_name[1], surname=full_name[2], telegram_id=message.from_user.id)
        await message.answer(
            """
    <b>Пользовательское соглашение для Telegram бота</b>
    """, reply_markup=confirm_keyboard, parse_mode="html"
        )
        await state.set_state(RegistrationStates.confirmation)
    except IndexError or AttributeError as e:
        await bot.send_message(message.from_user.id, "У вас неправильный формат!")
        await message.answer(f"Введи свое имя в формате:\n\nИмя Фамилия Отчество\n\nЧерез пробел!")


@dp.callback_query(RegistrationStates.confirmation)
async def confirmation_query(callback_query: types.CallbackQuery, state: FSMContext):
    confirm_data = callback_query.data
    await callback_query.message.delete()

    if confirm_data == "true":
        await bot.send_message(callback_query.from_user.id, "Отправьте ваш контакт", reply_markup=contact_keyboard)

        await state.update_data(is_confirm=confirm_data)

        await state.set_state(RegistrationStates.phone_number)

    else:
        await bot.send_message(callback_query.from_user.id, "Cancel")
        await state.clear()


@dp.message(RegistrationStates.phone_number, F.contact)
async def process_contact(message: types.Message, state: FSMContext):
    contact = message.contact
    await state.update_data(phone_number=contact.phone_number)

    data = await fetch_place_data(TOKEN)
    
    options = [{'name': item['name'], 'callback_data': str(item['id'])} for item in data]

    await send_place(message, options)

    await state.set_state(RegistrationStates.place)


@dp.callback_query(RegistrationStates.place)
async def callback_query_process_place(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(place=callback_query.data)
    await callback_query.message.delete()

    context = await state.get_data()
    print(context)

    try:
        data = await post_user_info(data=context, token=TOKEN)
        if data == 201:
            await bot.send_message(callback_query.from_user.id, "Спасибо за регистрацию!", reply_markup=profile_view_keyboard)
            await state.clear()
        else:
            await bot.send_message(callback_query.from_user.id, "Что-то пошло не так!", reply_markup=register_keyboard)
    except Exception as e:
        print(e)
        await bot.send_message(callback_query.from_user.id, "Что-то пошло не так!", reply_markup=register_keyboard)
    
    await state.set_state()


@dp.message()
async def registration_start(message: types.Message, state: FSMContext):
    message_answer = message.text
    if message_answer == "Профиль":
        user_data = await get_user_data(message.from_user.id, token=TOKEN)
        if user_data != None:
            status = "Активен🟢" if user_data["is_active"] == True else "Неактивен🔴"
            await message.answer(f"Имя: {user_data['first_name']}\nФамилия: {user_data['last_name']}\nОтчество: {user_data['surname']}\nНомер телефона: {user_data['phone_number']}\nСтатус: {status}", reply_markup=delete_keyboard)
            await state.set_state(ProfileState.profile)
        else:
            await message.answer("вы ещё не регистрировались", reply_markup=register_keyboard)
    elif message_answer == "Пройти Регистрацию":
        status = await user_exist(message.from_user.id, token=TOKEN)
        if status == 200:
            await message.answer(f"Вы уже регистрировались!", reply_markup=profile_view_keyboard)
        else:
            await message.answer(f"Давай начнем процесс регистрации. Введи свое имя в формате:\n\nИмя Фамилия Отчество\n\nЧерез пробел!")
            await state.set_state(RegistrationStates.name)
    elif message_answer == "Помощь":
        await message.answer(f"link to operator", reply_markup=profile_view_keyboard)
    elif message_answer == "Назад":
        await message.answer(f"Главная менью\n\nВоспользуйтесь кнопками", reply_markup=profile_view_keyboard)
    else:
        await message.answer("Для полной информации введите комманду /help")


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
