import asyncio
import os
import logging
import requests

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.methods import DeleteWebhook
from states.states import RegistrationStates, ProfileState, OrderState
from fetches.fetch import fetch_place_data, post_user_info, user_exist, get_user_data, delete_user_data, user_change_column, get_orders, take_order
from keyboards.keyboard import contact_keyboard, confirm_keyboard, delete_keyboard, register_keyboard, profile_view_keyboard, profile_column_keyboard, complete_keyboard


load_dotenv()
logging.basicConfig(level=logging.INFO)

TOKEN = os.environ['WORKER-TOKEN']
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


async def send_place(message, options):
    kb = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text=item['name'], callback_data=item['callback_data'])] for item in options]) # one line button one item 

    await bot.send_message(message.from_user.id, "Выберите район:", reply_markup=kb)


async def send_orders(callback_query, orders):
    callback_data = int(callback_query.data)

    for order in orders:

        if callback_data == order['place']:
            order_id = str(order['id'])

            order_keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text="Принять✅", callback_data=order_id)]])
            await bot.send_location(callback_query.from_user.id, latitude=order['latitude'], longitude=order['longitude'], reply_markup=order_keyboard)



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


@dp.callback_query(OrderState.order_view)
async def order_view_process(callback_query: types.CallbackQuery, state: FSMContext):
    orders = await get_orders(TOKEN)
    await send_orders(callback_query=callback_query, orders=orders)
    await state.set_state(OrderState.order_get)


@dp.callback_query(OrderState.order_get)
async def order_get_process(callback_query: types.CallbackQuery, state: FSMContext):
    order_id = callback_query.data
    data = {
        "worker_id": callback_query.from_user.id,
        "is_taken": "true"
    }
    take = await take_order(order_id=order_id, data=data, token=TOKEN)
    
    if take != None:
        photo = f"../client_bot/{take['client_photo']}"
        
        await bot.send_message(callback_query.from_user.id, "Заказ принят\n\nДанные заказа:")
        await bot.send_photo(callback_query.from_user.id, photo=types.FSInputFile(photo))
        await bot.send_location(callback_query.from_user.id, latitude=take['latitude'], longitude=take['longitude'])
        await bot.send_message(callback_query.from_user.id, f"Дом: {take['house_number']}\nКвартира: {take['apartment_number']}\nПодъезд: {take['entrance_number']}\nЭтаж: {take['floor_number']}\nКомментарии: {take['comment_to_address']}", reply_markup=complete_keyboard)
        await state.update_data(order_id=order_id)
        await state.set_state(OrderState.order_complete)


@dp.callback_query(OrderState.order_complete)
async def order_complete_process(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    data = await state.get_data()
    order_id = data.get("order_id")
    data = {
        "is_completed": "true"
    }
    if callback_data == "complete":
        take = await take_order(order_id=order_id, data=data, token=TOKEN)
        if take != None:
            await bot.send_message(callback_query.from_user.id, "Отправьте подтверждающую фотографию:")
            await state.set_state(OrderState.order_accept_photo)


@dp.message(F.photo, OrderState.order_accept_photo)
async def order_accept_process(message: types.Message, state: FSMContext):
    photo_data = message.photo[-1]
    file_id = photo_data.file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path

    data = await state.get_data()
    order_id = data.get("order_id")

    file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

    response = requests.get(file_url)

    if response.status_code == 200:
        photo_dir = f"accept/photo/{order_id}-{message.from_user.id}.jpg"
        # Открываем файл для записи в бинарном режиме и записываем в него содержимое ответа
        with open(photo_dir, "wb") as file:
            file.write(response.content)
        data = {
            "worker_photo": photo_dir
        }
        take = await take_order(order_id=order_id, data=data, token=TOKEN)
        if take != None:
            await message.answer("Заказ успешно закрыт", reply_markup=profile_view_keyboard)
    else:
        await message.answer("Ошибка при загрузке фотографии!")


@dp.callback_query(ProfileState.change)
async def change_process(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    await state.set_state(ProfileState.change_process)
    await callback_query.message.delete()
    if callback_data == "name":
        await bot.send_message(callback_query.from_user.id, "Введите новое имя:")
        await state.update_data(column_name="first_name")
    elif callback_data == "last_name":
        await bot.send_message(callback_query.from_user.id, "Введите Фамилию:")
        await state.update_data(column_name="last_name")
    elif callback_data == "surname":
        await bot.send_message(callback_query.from_user.id, "Введите Отчество:")
        await state.update_data(column_name="surname")


@dp.message(ProfileState.change_process)
async def name_change_process(message: types.Message, state: FSMContext):
    new_value = message.text
    callback_context = await state.get_data()
    column_name = callback_context.get("column_name")
    context = {
        column_name: new_value
    }
    status = await user_change_column(telegram_id=message.from_user.id, data=context, token=TOKEN)
    if status == 200:
        await message.answer(f"Данные успешно изменены!", reply_markup=profile_view_keyboard)
        await state.clear()
    else:
        await message.answer("Что-то пошло не так!", reply_markup=profile_view_keyboard)
        await state.clear()


@dp.message()
async def registration_start(message: types.Message, state: FSMContext):
    message_answer = message.text
    if message_answer == "Профиль":
        user_data = await get_user_data(message.from_user.id, token=TOKEN)
        if user_data != None:
            status = "Активен🟢" if user_data["is_active"] == True else "Неактивен🔴"
            await message.answer(f"Имя: {user_data['first_name']}\nФамилия: {user_data['last_name']}\nОтчество: {user_data['surname']}\nНомер телефона: {user_data['phone_number']}\nСтатус: {status}", reply_markup=delete_keyboard)
        else:
            await message.answer("вы ещё не регистрировались", reply_markup=register_keyboard)
    elif message_answer == "Пройти Регистрацию":
        status = await user_exist(message.from_user.id, token=TOKEN)
        if status == 200:
            await message.answer(f"Вы уже регистрировались!", reply_markup=profile_view_keyboard)
        else:
            await message.answer(f"Давай начнем процесс регистрации. Введи свое имя в формате:\n\nИмя Фамилия Отчество\n\nЧерез пробел!")
            await state.set_state(RegistrationStates.name)
    elif message_answer == "Редакторовать профиль":
        await message.answer("Выберите поле которое вы хотите изменить:", reply_markup=profile_column_keyboard)
        await state.set_state(ProfileState.change)
    elif message_answer == "Удалить аккаунт❌":
        delete_response = await delete_user_data(message.from_user.id, token=TOKEN)
        if delete_response == 204:
            await message.delete()
            await bot.send_message(message.from_user.id, "Аккаунт успешно удалён!")
        else:
            await bot.send_message(message.from_user.id, "Что-то пошло не так!")
    elif message_answer == "Взять заказ":
        data = await fetch_place_data(TOKEN)

        options = [{'name': item['name'], 'callback_data': str(item['id'])} for item in data]

        await send_place(message, options)
        await state.set_state(OrderState.order_view)
    elif message_answer == "Помощь":
        await message.answer(f"link to operator", reply_markup=profile_view_keyboard)
    elif message_answer == "◀️Назад":
        await message.answer(f"Главная менью\n\nВоспользуйтесь кнопками", reply_markup=profile_view_keyboard)
    else:
        await message.answer("Главная менью\n\nВоспользуйтесь кнопками", reply_markup=profile_view_keyboard)


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
