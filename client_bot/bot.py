import asyncio
import os
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.methods import DeleteWebhook
from states.states import RegistrationStates, ProfileState
from fetches.fetch import fetch_place_data, fetch_rates_data, post_user_info, user_exist, get_user_data, delete_user_data
from keyboards.keyboard import contact_keyboard, confirm_keyboard, delete_keyboard


load_dotenv()
logging.basicConfig(level=logging.INFO)

TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


async def send_place(chat_id, options):
    kb = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text=item['name'], callback_data=item['callback_data'])] for item in options]) # one line button one item 

    await bot.send_message(chat_id, "Выберите район:", reply_markup=kb)


async def send_rates(chat_id, options):
    kb = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text=item['name'], callback_data=item['callback_data'])] for item in options], row_width=1)

    await bot.send_message(chat_id, "Выберите тариф:", reply_markup=kb)


@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(f"/start (приветствие и общая информация и информация о командах )\n/registration - Регистрация\n/help")


@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(f"/help link to operator")


@dp.message(Command("profile"))
async def profile_command(message: types.Message, state: FSMContext):
    user_data = await get_user_data(message.from_user.id, token=TOKEN)
    if user_data != None:
        await message.answer(f"имя: {user_data['name']}\nномер телефона: {user_data['phone_number']}\nномер дома: {user_data['house_number']}\nномер квартиры: {user_data['apartment_number']}\nномер подьезда: {user_data['entrance_number']}\nэтаж: {user_data['floor_number']}\nкомментарии к адресу: {user_data['comment_to_address']}", reply_markup=delete_keyboard)
        await state.set_state(ProfileState.profile)
    else:
        await message.answer("вы ещё не регистрировалась")


@dp.callback_query(ProfileState.profile)
async def delete_process(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    if callback_data == "delete":
        delete_data = await delete_user_data(callback_query.from_user.id, token=TOKEN)
        print(delete_data)


@dp.message(Command("registration"))
async def registration_start(message: types.Message, state: FSMContext):
    status = await user_exist(message.from_user.id, token=TOKEN)
    print(status)
    if status == 200:
        await message.answer(f"Вы уже регистрировались!")
    else:
        await message.answer(f"Давай начнем процесс регистрации. Введи свое имя:")
        await state.set_state(RegistrationStates.name)


@dp.message(RegistrationStates.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text, telegram_id=message.from_user.id)
    await message.answer(
        """
<b>Пользовательское соглашение для Telegram бота</b>

Пожалуйста, обратите внимание, что следующее пользовательское соглашение представляет собой общие правила и условия использования Telegram бота, занимающегося коммерцией в сфере услуг. Эти условия описывают взаимоотношения между владельцем бота и его пользователями. Пожалуйста, внимательно прочитайте их перед использованием бота.

<b>1. Предоставление услуг</b>
   1.1. Владелец бота предлагает услуги через Telegram бота и обязуется предоставлять их в соответствии с описанием услуг, предоставленным в боте.
   1.2. Владелец бота оставляет за собой право изменять, обновлять или прекращать предоставление любых услуг в любое время без предварительного уведомления пользователя.

<b>2. Ограничение ответственности</b>
   2.1. Владелец бота не несет ответственности за любые прямые или косвенные убытки, понесенные пользователями в результате использования услуг, предоставляемых ботом.
   2.2. Владелец бота не несет ответственности за проблемы, возникающие из-за неправильного использования бота или неправильной интерпретации предоставленной информации.
   2.3. Владелец бота не несет ответственности за любые проблемы, связанные с Telegram платформой или взаимодействием с другими ботами или сторонними сервисами.

<b>3. Конфиденциальность</b>
   3.1. Владелец бота обязуется обрабатывать персональные данные пользователей в соответствии с применимым законодательством о защите данных.
   3.2. Владелец бота не будет передавать персональные данные пользователей третьим лицам без их предварительного согласия, за исключением случаев, предусмотренных законодательством.

<b>4. Интеллектуальная собственность</b>
   4.1. Все права на интеллектуальную собственность, связанную с ботом (включая, но не ограничиваясь, авторскими правами и товарными знаками), принадлежат владельцу бота.
   4.2. Пользователи не имеют права использовать, копировать, изменять или распространять содержимое бота без предварительного письменного согласия владельца бота.

<b>5. Запрет на злоупотребление</b>
   5.1. Пользователям запрещено использовать бота для распространения незаконного, вредоносного или оскорбительного содержимого.
   5.2. Пользователям запрещено использовать бота для осуществления мошенничества, спама или любых других действий, которые могут повредить владельцу бота или другим пользователям.

<b>6. Изменение пользовательского соглашения</b>
   6.1. Владелец бота оставляет за собой право в любое время изменять условия данного пользовательского соглашения.
   6.2. Измененное пользовательское соглашение будет опубликовано в боте или предоставлено пользователямв виде уведомления. Пользователи обязуются периодически проверять пользовательское соглашение на наличие изменений.

<b>7. Прекращение использования</b>
   7.1. Пользователи могут прекратить использование бота в любое время.
   7.2. Владелец бота оставляет за собой право прекратить предоставление услуг пользователям в случае нарушения пользователем условий данного пользовательского соглашения или в случае несоответствия действиям пользователя законодательству или морально-этическим нормам.

<b>8. Применимое право и разрешение споров</b>
   8.1. Данное пользовательское соглашение регулируется и толкуется в соответствии с законодательством страны, в которой зарегистрирован владелец бота.
   8.2. Любые споры, возникающие между владельцем бота и пользователями, будут разрешаться путем переговоров и сотрудничества. В случае невозможности достижения согласия, споры будут переданы на рассмотрение компетентного суда.

Пожалуйста, имейте в виду, что данное пользовательское соглашение является лишь общими правилами и условиями использования бота. Владелец бота может также иметь дополнительные политики и условия, которые могут быть доступны в боте или на его веб-сайте.
""", reply_markup=confirm_keyboard, parse_mode="html"
    )
    await state.set_state(RegistrationStates.confirmation)


@dp.callback_query(RegistrationStates.confirmation)
async def confirmation_query(callback_query: types.CallbackQuery, state: FSMContext):
    confirm_data = callback_query.data

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

    await send_place(message.from_user.id, options)

    await state.set_state(RegistrationStates.place)


@dp.callback_query(RegistrationStates.place)
async def callback_query_process_place(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(place=callback_query.data)
    data = await fetch_rates_data(TOKEN)

    options = [{'name': item['rate_name'], 'callback_data': str(item['id'])} for item in data]

    await send_rates(callback_query.from_user.id, options)

    await state.set_state(RegistrationStates.rate)


@dp.callback_query(RegistrationStates.rate)
async def callback_query_process_rate(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(rate=callback_query.data)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[types.KeyboardButton(text="Отправить локацию", request_location=True)]], one_time_keyboard=True)
    await bot.send_message(callback_query.from_user.id, "Отправьте локацию:", reply_markup=keyboard)
    await state.set_state(RegistrationStates.location)


@dp.message(RegistrationStates.location, F.location)
async def handle_location(message: types.Message, state: FSMContext):
    latitude = message.location.latitude
    longitude = message.location.longitude

    await state.update_data(latitude=latitude, longitude=longitude)

    await bot.send_message(message.from_user.id, "Отправьте номер дома:")
    await state.set_state(RegistrationStates.house)


@dp.message(RegistrationStates.house)
async def process_house(message: types.Message, state: FSMContext):
    await state.update_data(house_number=message.text)
    await bot.send_message(message.from_user.id, "Отправьте номер квартиры:")
    await state.set_state(RegistrationStates.apartment)


@dp.message(RegistrationStates.apartment)
async def process_apartment(message: types.Message, state: FSMContext):
    await state.update_data(apartment_number=message.text)
    await bot.send_message(message.from_user.id, "Отправьте номер подьезда:")
    await state.set_state(RegistrationStates.entrance)


@dp.message(RegistrationStates.entrance)
async def process_entrance(message: types.Message, state: FSMContext):
    await state.update_data(entrance_number=message.text)
    await bot.send_message(message.from_user.id, "Отправьте номер этажа:")
    await state.set_state(RegistrationStates.floor)


@dp.message(RegistrationStates.floor)
async def process_floor(message: types.Message, state: FSMContext):
    await state.update_data(floor_number=message.text)
    await bot.send_message(message.from_user.id, "Комментарии к адресу:")
    await state.set_state(RegistrationStates.comment)


@dp.message(RegistrationStates.comment)
async def process_comment(message: types.Message, state: FSMContext):
    await state.update_data(comment_to_address=message.text)

    context = await state.get_data()

    try:
        await post_user_info(data=context, token=TOKEN)
        
        await bot.send_message(message.from_user.id, "Спасибо за регистрацию!")
        await state.clear()
    except Exception as e:
        print(e)
        await bot.send_message(message.from_user.id, "Что-то пошло не так!")


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
