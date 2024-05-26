import asyncio
import os
import logging
import requests

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.methods import DeleteWebhook
from translation.localization import Localization
from states.states import (
    RegistrationStates,
    ProfileState,
    OrderCreate,
    LanguageChange
)
from fetches.fetch import (
    fetch_place_data,
    fetch_rates_data,
    post_user_info,
    user_exist,
    get_user_data,
    delete_user_data,
    user_change_column,
    create_order,
    order_exist,
    take_order,
    post_user_language,
    user_language
)
from keyboards.keyboard import (
    contact_keyboard,
    confirm_keyboard,
    delete_keyboard,
    register_keyboard,
    location_keyboard,
    profile_view_keyboard,
    profile_column_keyboard,
    language_keyboard
)

load_dotenv()
# logging.basicConfig(level=logging.INFO, filename="client_log.log")
logging.basicConfig(level=logging.INFO)

TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

scheduler = AsyncIOScheduler(timezone='Asia/Tashkent')


# Функция для отправки локализованных сообщений
async def get_localized_message(language, key):
    translation = Localization.get_translation(language, key)
    return translation


async def send_place(message, options, language):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[[types.InlineKeyboardButton(text=item['name'], callback_data=item['callback_data'])] for item
                         in options])
    localized_message = await get_localized_message(language=language, key="get_place")

    await bot.send_message(message.from_user.id, localized_message, reply_markup=kb)


async def send_rates(chat_id, options, language):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[[types.InlineKeyboardButton(text=item['name'], callback_data=item['callback_data'])] for item
                         in options], row_width=1)

    localized_message = await get_localized_message(language=language, key="get_rate")

    await bot.edit_message_text(localized_message, chat_id.message.chat.id, chat_id.message.message_id, reply_markup=kb)


async def send_message_scheduler(chat_id):
    await bot.send_message(chat_id, "Test message scheduler")


async def scheduler_daily_message(chat_id, hour, minute):
    trigger = CronTrigger(hour=hour, minute=minute)
    scheduler.add_job(send_message_scheduler, trigger, args=[chat_id])


@dp.message(CommandStart())
async def start_command(message: types.Message, state: FSMContext):
    user_data = await get_user_data(message.from_user.id, token=TOKEN)

    if user_data is not None:
        user_id = message.from_user.id
        language_data = await user_language(user_id=user_id, token=TOKEN)
        language_code = language_data['lang']

        localized_message = await get_localized_message(language_code, "greeting_registered")

        localized_btn_1 = await get_localized_message(language_code, "profile_btn")
        localized_btn_2 = await get_localized_message(language_code, "create_order_btn")
        localized_btn_3 = await get_localized_message(language_code, "actual_order_btn")
        localized_btn_4 = await get_localized_message(language_code, "change_language_btn")
        localized_btn_5 = await get_localized_message(language_code, "help_btn")
        profile_btn = await profile_view_keyboard(localized_btn_1, localized_btn_2, localized_btn_3, localized_btn_4,
                                                  localized_btn_5)
        await message.answer(localized_message, reply_markup=profile_btn)
        await state.clear()
    else:
        language_btn = await language_keyboard()
        welcome_message = await get_localized_message("none", "welcome")
        await message.answer(welcome_message, reply_markup=language_btn)
        await state.set_state(RegistrationStates.get_language)


@dp.callback_query(RegistrationStates.get_language)
async def get_language(callback_query: types.CallbackQuery, state: FSMContext):
    language_code = callback_query.data

    context = {
        "user_id": callback_query.from_user.id,
        "lang": language_code
    }
    post_lang = await post_user_language(data=context, token=TOKEN)

    if post_lang == 201 or post_lang == 200:
        localized_message = await get_localized_message(language=language_code, key="greeting_not_registered")
        localized_message_btn_1 = await get_localized_message(language=language_code, key="register_btn")
        localized_message_btn_2 = await get_localized_message(language=language_code, key="help_btn")
        register_btn = await register_keyboard(localized_message_btn_1, localized_message_btn_2)
        await callback_query.message.answer(localized_message, reply_markup=register_btn)
        await state.clear()
    else:
        error_message = await get_localized_message("none", "error")
        await callback_query.message.answer(error_message)


@dp.message(ProfileState.profile)
async def delete_process(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    language_data = await user_language(user_id=user_id, token=TOKEN)
    language_code = language_data['lang']
    answer = message.text
    if answer == "Удалить аккаунт❌" or answer == "Akkauntni ochirish":
        delete_response = await delete_user_data(message.from_user.id, token=TOKEN)
        if delete_response == 204:
            await message.delete()
            await bot.send_message(message.from_user.id, "Аккаунт успешно удалён!")
        else:
            await bot.send_message(message.from_user.id, "Что-то пошло не так!")
        await state.clear()
    elif answer == "Редакторовать профиль" or answer == "Profilni sozlash":
        localized_message = await get_localized_message(language_code, "change_profile")
        localized_btn_1 = await get_localized_message(language_code, "name_btn")
        localized_btn_2 = await get_localized_message(language_code, "house_number_btn")
        localized_btn_3 = await get_localized_message(language_code, "apartment_number_btn")
        localized_btn_4 = await get_localized_message(language_code, "entrance_number_btn")
        localized_btn_5 = await get_localized_message(language_code, "floor_number_btn")
        localized_btn_6 = await get_localized_message(language_code, "comment_btn")
        profile_column_btn = await profile_column_keyboard(
            localized_btn_1,
            localized_btn_2,
            localized_btn_3,
            localized_btn_4,
            localized_btn_5,
            localized_btn_6
        )
        await message.answer(localized_message, reply_markup=profile_column_btn)
        await state.set_state(ProfileState.change)


@dp.callback_query(ProfileState.change)
async def change_process(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    language_data = await user_language(user_id=user_id, token=TOKEN)
    language_code = language_data['lang']
    callback_data = callback_query.data
    await state.set_state(ProfileState.change_process)
    await callback_query.message.delete()
    if callback_data == "name":
        localized_message = await get_localized_message(language_code, "change_name_message")
        await bot.send_message(callback_query.from_user.id, localized_message)
        await state.update_data(column_name="name")
    elif callback_data == "house_number":
        localized_message = await get_localized_message(language_code, "change_house_message")
        await bot.send_message(callback_query.from_user.id, localized_message)
        await state.update_data(column_name="house_number")
    elif callback_data == "apartment_number":
        localized_message = await get_localized_message(language_code, "change_apartment_message")
        await bot.send_message(callback_query.from_user.id, localized_message)
        await state.update_data(column_name="apartment_number")
    elif callback_data == "entrance_number":
        localized_message = await get_localized_message(language_code, "change_entrance_message")
        await bot.send_message(callback_query.from_user.id, localized_message)
        await state.update_data(column_name="entrance_number")
    elif callback_data == "floor_number":
        localized_message = await get_localized_message(language_code, "change_floor_message")
        await bot.send_message(callback_query.from_user.id, localized_message)
        await state.update_data(column_name="floor_number")
    elif callback_data == "comment_to_address":
        localized_message = await get_localized_message(language_code, "change_comment_message")
        await bot.send_message(callback_query.from_user.id, localized_message)
        await state.update_data(column_name="comment_to_address")
    else:
        localized_message = await get_localized_message(language_code, "error_changing")
        localized_btn_1 = await get_localized_message(language_code, "name_btn")
        localized_btn_2 = await get_localized_message(language_code, "house_number_btn")
        localized_btn_3 = await get_localized_message(language_code, "apartment_number_btn")
        localized_btn_4 = await get_localized_message(language_code, "entrance_number_btn")
        localized_btn_5 = await get_localized_message(language_code, "floor_number_btn")
        localized_btn_6 = await get_localized_message(language_code, "comment_btn")
        profile_column_btn = await profile_column_keyboard(
            localized_btn_1,
            localized_btn_2,
            localized_btn_3,
            localized_btn_4,
            localized_btn_5,
            localized_btn_6
        )
        await bot.send_message(callback_query.from_user.id, localized_message, reply_markup=profile_column_btn)
        await state.set_state(ProfileState.change)


@dp.message(ProfileState.change_process)
async def name_change_process(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    language_data = await user_language(user_id=user_id, token=TOKEN)
    language_code = language_data['lang']
    new_name = message.text
    callback_context = await state.get_data()
    column_name = callback_context.get("column_name")
    context = {
        column_name: new_name
    }
    status = await user_change_column(telegram_id=message.from_user.id, data=context, token=TOKEN)
    localized_btn_1 = await get_localized_message(language_code, "profile_btn")
    localized_btn_2 = await get_localized_message(language_code, "create_order_btn")
    localized_btn_3 = await get_localized_message(language_code, "actual_order_btn")
    localized_btn_4 = await get_localized_message(language_code, "change_language_btn")
    localized_btn_5 = await get_localized_message(language_code, "help_btn")
    profile_btn = await profile_view_keyboard(localized_btn_1, localized_btn_2, localized_btn_3, localized_btn_4,
                                              localized_btn_5)
    if status == 200:
        localized_message = await get_localized_message(language_code, "complete_changing")
        await message.answer(localized_message, reply_markup=profile_btn)
        await state.clear()
    else:
        localized_message = await get_localized_message(language_code, "error")
        await message.answer(localized_message, reply_markup=profile_btn)
        await state.clear()


@dp.message(RegistrationStates.name)
async def process_name(message: types.Message, state: FSMContext):
    chat_id = message.from_user.id

    language_data = await user_language(user_id=chat_id, token=TOKEN)
    language_code = language_data['lang']

    try:
        localized_message = await get_localized_message(language=language_code, key="confirmation")
        localized_btn_1 = await get_localized_message(language_code, "confirm_btn")
        localized_btn_2 = await get_localized_message(language_code, "cancel_btn")
        confirm_btn = await confirm_keyboard(localized_btn_1, localized_btn_2)
        full_name = message.text.split(" ")
        await state.update_data(name=full_name[1], last_name=full_name[0], surname=full_name[2],
                                telegram_id=message.from_user.id)
        await message.answer(localized_message, reply_markup=confirm_btn, parse_mode="html")
        await state.set_state(RegistrationStates.confirmation)
    except IndexError or AttributeError as e:
        localized_message = await get_localized_message(language=language_code, key="error_name_format")
        await message.answer(localized_message)
        logging.error(e)


@dp.callback_query(RegistrationStates.confirmation)
async def confirmation_query(callback_query: types.CallbackQuery, state: FSMContext):
    confirm_data = callback_query.data
    chat_id = callback_query.from_user.id
    await callback_query.message.delete()

    language_data = await user_language(user_id=chat_id, token=TOKEN)
    language_code = language_data['lang']

    if confirm_data == "true":
        localized_btn = await get_localized_message(language=language_code, key="get_contact_btn")
        contact_btn = await contact_keyboard(localized_btn)
        localized_message = await get_localized_message(language=language_code, key="get_contact")
        await bot.send_message(callback_query.from_user.id, localized_message, reply_markup=contact_btn)
        await state.update_data(is_confirm=confirm_data)
        await state.set_state(RegistrationStates.phone_number)

    else:
        await bot.send_message(callback_query.from_user.id, "Cancel")
        await state.clear()


@dp.message(RegistrationStates.phone_number, F.contact)
async def process_contact(message: types.Message, state: FSMContext):
    contact = message.contact
    await state.update_data(phone_number=contact.phone_number)
    chat_id = message.from_user.id

    language_data = await user_language(user_id=chat_id, token=TOKEN)
    language_code = language_data['lang']

    place_data = await fetch_place_data(TOKEN)

    options = [{'name': item['name'], 'callback_data': str(item['id'])} for item in place_data]

    await send_place(message, options, language_code)

    await state.set_state(RegistrationStates.place)


@dp.callback_query(RegistrationStates.place)
async def callback_query_process_place(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(place=callback_query.data)
    chat_id = callback_query.from_user.id

    language_data = await user_language(user_id=chat_id, token=TOKEN)
    language_code = language_data['lang']

    rates_data = await fetch_rates_data(TOKEN)

    options = [{'name': item['rate_name'], 'callback_data': str(item['id'])} for item in rates_data]

    await send_rates(callback_query, options, language_code)

    await state.set_state(RegistrationStates.rate)


@dp.callback_query(RegistrationStates.rate)
async def callback_query_process_rate(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(rate=callback_query.data)
    await callback_query.message.delete()
    chat_id = callback_query.from_user.id

    language_data = await user_language(user_id=chat_id, token=TOKEN)
    language_code = language_data['lang']

    localized_message = await get_localized_message(language=language_code, key="get_location")
    localized_btn = await get_localized_message(language=language_code, key="get_location_btn")
    location_btn = await location_keyboard(localized_btn)
    await bot.send_message(callback_query.from_user.id, localized_message, reply_markup=location_btn)
    await state.set_state(RegistrationStates.location)


@dp.message(RegistrationStates.location, F.location)
async def handle_location(message: types.Message, state: FSMContext):
    latitude = message.location.latitude
    longitude = message.location.longitude

    chat_id = message.from_user.id

    language_data = await user_language(user_id=chat_id, token=TOKEN)
    language_code = language_data['lang']

    await state.update_data(latitude=latitude, longitude=longitude)

    localized_message = await get_localized_message(language=language_code, key="get_address")
    message_id = await bot.send_message(message.from_user.id, localized_message)
    await state.update_data(message_id=message_id.message_id)
    await state.set_state(RegistrationStates.home)


@dp.message(RegistrationStates.home)
async def process_house_data(message: types.Message, state: FSMContext):
    chat_id = message.from_user.id

    language_data = await user_language(user_id=chat_id, token=TOKEN)
    language_code = language_data['lang']

    try:
        list_data = message.text.split("/")

        await state.update_data(house_number=list_data[0], apartment_number=list_data[1], entrance_number=list_data[2],
                                floor_number=list_data[3])
        await message.delete()

        data = await state.get_data()
        localized_message = await get_localized_message(language=language_code, key="get_comment_to_address")
        message_id = data.get("message_id")
        message_id = await bot.edit_message_text(localized_message, message.chat.id, message_id)

        await state.update_data(message_id=message_id.message_id)
        await state.set_state(RegistrationStates.comment)
    except IndexError or AttributeError as e:
        localized_message = await get_localized_message(language=language_code, key="error_address_format")
        message_id = await bot.send_message(message.from_user.id, localized_message)
        await state.update_data(message_id=message_id.message_id)
        logging.error(e)


@dp.message(RegistrationStates.comment)
async def process_comment(message: types.Message, state: FSMContext):
    await state.update_data(comment_to_address=message.text)
    await message.delete()

    data = await state.get_data()
    chat_id = message.from_user.id

    language_data = await user_language(user_id=chat_id, token=TOKEN)
    language_code = language_data['lang']

    try:
        await post_user_info(data=data, token=TOKEN)
        localized_message = await get_localized_message(language_code, "complete_registration")
        localized_btn_1 = await get_localized_message(language_code, "profile_btn")
        localized_btn_2 = await get_localized_message(language_code, "create_order_btn")
        localized_btn_3 = await get_localized_message(language_code, "actual_order_btn")
        localized_btn_4 = await get_localized_message(language_code, "change_language_btn")
        localized_btn_5 = await get_localized_message(language_code, "help_btn")
        profile_btn = await profile_view_keyboard(localized_btn_1, localized_btn_2, localized_btn_3, localized_btn_4,
                                                  localized_btn_5)
        await bot.send_message(message.from_user.id, localized_message, reply_markup=profile_btn)
        await state.clear()
    except Exception as e:
        localized_message_btn_1 = await get_localized_message(language_code, "register_btn")
        localized_message_btn_2 = await get_localized_message(language_code, "help_btn")
        register_btn = await register_keyboard(localized_message_btn_1, localized_message_btn_2)
        localized_message = await get_localized_message(language_code, "error")
        await bot.send_message(message.from_user.id, localized_message, reply_markup=register_btn)
        logging.error(e)


@dp.message(F.photo, OrderCreate.photo)
async def get_accept_photo_process(message: types.Message, state: FSMContext):
    photo_data = message.photo[-1]
    file_id = photo_data.file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path

    file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

    data = await state.get_data()
    order_id = data.get("order_id")

    chat_id = message.from_user.id

    language_data = await user_language(user_id=chat_id, token=TOKEN)
    language_code = language_data['lang']

    # Отправляем GET-запрос для загрузки файла
    response = requests.get(file_url)

    if response.status_code == 200:
        photo_dir = f"accept/photo/{order_id}-{message.from_user.id}.jpg"
        # Открываем файл для записи в бинарном режиме и записываем в него содержимое ответа
        with open(photo_dir, "wb") as file:
            file.write(response.content)
        user = await get_user_data(message.from_user.id, token=TOKEN)
        rate_count = int(user["rate_count"])
        if user is not None:
            if rate_count < 1:
                localized_message = await get_localized_message(language_code, "rate_count_error")
                await message.answer(localized_message)
                return
            new_count = rate_count - 1
            context = {
                "client_photo": photo_dir
            }
            user_context = {
                "rate_count": str(new_count)
            }
            order = await take_order(order_id=order_id, data=context, token=TOKEN)
            response_code = await user_change_column(message.from_user.id, data=user_context, token=TOKEN)
            localized_btn_1 = await get_localized_message(language_code, "profile_btn")
            localized_btn_2 = await get_localized_message(language_code, "create_order_btn")
            localized_btn_3 = await get_localized_message(language_code, "actual_order_btn")
            localized_btn_4 = await get_localized_message(language_code, "change_language_btn")
            localized_btn_5 = await get_localized_message(language_code, "help_btn")
            profile_btn = await profile_view_keyboard(localized_btn_1, localized_btn_2, localized_btn_3,
                                                      localized_btn_4,
                                                      localized_btn_5)
            if order is not None and response_code == 200:
                localized_message = await get_localized_message(language_code, "order_success")
                await message.answer(f"{localized_message} {new_count}",
                                     reply_markup=profile_btn)
            else:
                localized_message = await get_localized_message(language_code, "error")
                await message.answer(localized_message, reply_markup=profile_btn)
    else:
        localized_message = await get_localized_message(language_code, "photo_load_error")
        await message.answer(localized_message)

    await state.clear()


@dp.callback_query(LanguageChange.change)
async def change_language_process(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    chat_id = callback_query.from_user.id

    data = {
        "lang": callback_data
    }
    user_lang = await user_language(data=data, user_id=chat_id, token=TOKEN)
    if user_lang == 200:
        language_data = await user_language(user_id=chat_id, token=TOKEN)
        language_code = language_data['lang']

        localized_btn_1 = await get_localized_message(language_code, "profile_btn")
        localized_btn_2 = await get_localized_message(language_code, "create_order_btn")
        localized_btn_3 = await get_localized_message(language_code, "actual_order_btn")
        localized_btn_4 = await get_localized_message(language_code, "change_language_btn")
        localized_btn_5 = await get_localized_message(language_code, "help_btn")
        profile_btn = await profile_view_keyboard(localized_btn_1, localized_btn_2, localized_btn_3,
                                                  localized_btn_4, localized_btn_5)
        local_message = await get_localized_message(language_code, "change_language_success")
        await bot.send_message(chat_id, local_message, reply_markup=profile_btn)


@dp.message()
async def registration_start(message: types.Message, state: FSMContext):
    message_answer = message.text
    user_data = await get_user_data(message.from_user.id, token=TOKEN)
    chat_id = message.from_user.id

    language_data = await user_language(user_id=chat_id, token=TOKEN)
    language_code = language_data['lang']

    localized_btn_1 = await get_localized_message(language_code, "profile_btn")
    localized_btn_2 = await get_localized_message(language_code, "create_order_btn")
    localized_btn_3 = await get_localized_message(language_code, "actual_order_btn")
    localized_btn_4 = await get_localized_message(language_code, "change_language_btn")
    localized_btn_5 = await get_localized_message(language_code, "help_btn")
    profile_btn = await profile_view_keyboard(localized_btn_1, localized_btn_2, localized_btn_3, localized_btn_4,
                                              localized_btn_5)
    if message_answer == "Профиль" or message_answer == "Profil":

        if user_data is not None:
            loc_message_1 = await get_localized_message(language_code, "name")
            loc_message_2 = await get_localized_message(language_code, "phone_number")
            loc_message_3 = await get_localized_message(language_code, "house_number")
            loc_message_4 = await get_localized_message(language_code, "apartment_number")
            loc_message_5 = await get_localized_message(language_code, "entrance_number")
            loc_message_6 = await get_localized_message(language_code, "floor")
            loc_message_7 = await get_localized_message(language_code, "comment_to_address")
            loc_message_8 = await get_localized_message(language_code, "active")
            loc_message_9 = await get_localized_message(language_code, "not_active")
            loc_message_10 = await get_localized_message(language_code, "status")
            localized_btn_1 = await get_localized_message(language_code, "delete_btn")
            localized_btn_2 = await get_localized_message(language_code, "edit_btn")
            localized_btn_3 = await get_localized_message(language_code, "back_btn")
            profile_detail_btn = await delete_keyboard(localized_btn_1, localized_btn_2, localized_btn_3)
            status = loc_message_8 if user_data["is_active"] else loc_message_9
            await message.answer(
                f"{loc_message_1} {user_data['name']}\n{loc_message_2} {user_data['phone_number']}\n{loc_message_3} {user_data['house_number']}\n{loc_message_4} {user_data['apartment_number']}\n{loc_message_5} {user_data['entrance_number']}\n{loc_message_6} {user_data['floor_number']}\n{loc_message_7} {user_data['comment_to_address']}\n{loc_message_10} {status}",
                reply_markup=profile_detail_btn)
        else:
            localized_message = await get_localized_message(language=language_code, key="profile_error")
            localized_message_btn_1 = await get_localized_message(language=language_code, key="register_btn")
            localized_message_btn_2 = await get_localized_message(language=language_code, key="help_btn")
            register_btn = await register_keyboard(localized_message_btn_1, localized_message_btn_2)
            await message.answer(localized_message, reply_markup=register_btn)

    elif message_answer == "Пройти Регистрацию" or message_answer == "Ro'yhatdan o'tish":
        status = await user_exist(message.from_user.id, token=TOKEN)
        if status == 200:
            language_code = user_data.get("language_code")
            localized_message = await get_localized_message(language=language_code, key="already_registered")
            await message.answer(localized_message)
        else:
            localized_message = await get_localized_message(language=language_code, key="get_name")
            await message.answer(localized_message)
            await state.set_state(RegistrationStates.name)
            await state.update_data(language_code=language_code)

    elif message_answer == "Помощь" or message_answer == "Yordam":
        localized_message = await get_localized_message(language_code, "help_message")
        await message.answer(localized_message, reply_markup=profile_btn)

    elif message_answer == "◀️Назад" or message_answer == "◀️Orqaga":
        localized_message = await get_localized_message(language_code, "back_message")
        await message.answer(localized_message, reply_markup=profile_btn)

    elif message_answer == "Удалить аккаунт❌" or message_answer == "Akkaunt o'chirish❌":
        delete_response = await delete_user_data(message.from_user.id, token=TOKEN)
        if delete_response == 204:
            await message.delete()
            localized_message = await get_localized_message(language_code, "deleted_success")
            await bot.send_message(message.from_user.id, localized_message)
        else:
            localized_message = await get_localized_message(language_code, "error")
            await bot.send_message(message.from_user.id, localized_message)

    elif message_answer == "Редакторовать профиль" or message_answer == "Profilni tahrirlash":
        localized_message = await get_localized_message(language_code, "change_profile")
        localized_btn_1 = await get_localized_message(language_code, "name_btn")
        localized_btn_2 = await get_localized_message(language_code, "house_number_btn")
        localized_btn_3 = await get_localized_message(language_code, "apartment_number_btn")
        localized_btn_4 = await get_localized_message(language_code, "entrance_number_btn")
        localized_btn_5 = await get_localized_message(language_code, "floor_number_btn")
        localized_btn_6 = await get_localized_message(language_code, "comment_btn")
        profile_column_btn = await profile_column_keyboard(
            localized_btn_1,
            localized_btn_2,
            localized_btn_3,
            localized_btn_4,
            localized_btn_5,
            localized_btn_6
        )
        await message.answer(localized_message, reply_markup=profile_column_btn)
        await state.set_state(ProfileState.change)

    elif message_answer == "Создать заказ" or message_answer == "Buyurtma yaratish":
        order = await order_exist(message.from_user.id, token=TOKEN)
        if not order:
            rate_count = int(user_data["rate_count"])
            if rate_count < 1:
                localized_message = await get_localized_message(language_code, "rate_count_error")
                await message.answer(localized_message, reply_markup=profile_btn)
                return

            context = {
                "client_id": message.from_user.id
            }
            order = await create_order(data=context, token=TOKEN)

            if order is not None:
                localized_message = await get_localized_message(language_code, "accept_photo")
                await message.answer(localized_message)
                order_id = order['id']
                await state.update_data(order_id=order_id)
                await state.set_state(OrderCreate.photo)
            else:
                localized_message = await get_localized_message(language_code, "error")
                await message.answer(localized_message)
        else:
            localized_message = await get_localized_message(language_code, "not_ended_order_error")
            await message.answer(localized_message, reply_markup=profile_btn)

    elif message_answer == "Актуальный заказ" or message_answer == "Joriy buyurtma":
        order = await order_exist(message.from_user.id, token=TOKEN)
        if not order:
            localized_message = await get_localized_message(language_code, "not_order_error")
            await message.answer(localized_message, reply_markup=profile_btn)
        else:
            loc_message_1 = await get_localized_message(language_code, "worker_status")
            loc_message_2 = await get_localized_message(language_code, "order_created_time")
            loc_message_3 = await get_localized_message(language_code, "order_end")
            loc_message_4 = await get_localized_message(language_code, "order_not_end")
            loc_message_5 = await get_localized_message(language_code, "order_status")

            date = order['created_date']

            datetime_object = datetime.fromisoformat(date)

            time_only = datetime_object.strftime("%H:%M")

            status = loc_message_3 if order["is_completed"] else loc_message_4
            await message.answer(
                f"id: {order['id']}\n{loc_message_5} {status}\n{loc_message_1} {order['is_taken']}\n{loc_message_2} {time_only}",
                reply_markup=profile_btn)

    elif message_answer == "Изменить язык" or message_answer == "Tilni o'zgartirish":
        language_btn = await language_keyboard()
        local_message = await get_localized_message(language_code, "change_language")
        await message.answer(local_message, reply_markup=language_btn)
        await state.set_state(LanguageChange.change)

    else:
        localized_message = await get_localized_message(language_code, "default_message")
        await message.answer(localized_message)


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))

    await scheduler_daily_message(819233688, 23, 43)
    scheduler.start()

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.info("Start Service")
    asyncio.run(main())
    logging.info("Stop Service")
