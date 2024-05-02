import asyncio
import os
import logging
import requests

from datetime import datetime
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.methods import DeleteWebhook
from states.states import RegistrationStates, ProfileState, OrderCreate
from fetches.fetch import fetch_place_data, fetch_rates_data, post_user_info, user_exist, get_user_data, delete_user_data, user_change_column, create_order, order_exist
from keyboards.keyboard import contact_keyboard, confirm_keyboard, delete_keyboard, register_keyboard, location_keyboard, profile_view_keyboard, profile_column_keyboard


load_dotenv()
logging.basicConfig(level=logging.INFO)

TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


async def send_place(message, options):
    kb = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text=item['name'], callback_data=item['callback_data'])] for item in options]) 

    await bot.send_message(message.from_user.id, "Выберите район:", reply_markup=kb)


async def send_rates(chat_id, options):
    kb = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text=item['name'], callback_data=item['callback_data'])] for item in options], row_width=1)

    await bot.edit_message_text("Выберите тариф:", chat_id.message.chat.id, chat_id.message.message_id, reply_markup=kb)


@dp.message(CommandStart())
async def start_command(message: types.Message, state: FSMContext):
    user_data = await get_user_data(message.from_user.id, token=TOKEN)

    if user_data != None:
        await message.answer("""
Для пользования бота можете использовать следующие комманды:

/start - Для начала использования или для рестарта
                             
Нажмите на кнопку - Профиль - для полной информации вашего аккаунта
Нажмите на кнопку - Помощь - что бы связаться с администратором
                             """, reply_markup=profile_view_keyboard)
    else:
        await message.answer(f"""
Для пользования бота можете использовать следующие комманды:

/start - Для начала использования или для рестарта
                             
Что бы пройти регистрацию нажмите на кнопку
Нажмите на кнопку - Помощь - что бы связаться с администратором
                             """, reply_markup=register_keyboard)
    await state.clear()


@dp.message(ProfileState.profile)
async def delete_process(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == "Удалить аккаунт❌":
        delete_response = await delete_user_data(message.from_user.id, token=TOKEN)
        if delete_response == 204:
            await message.delete()
            await bot.send_message(message.from_user.id, "Аккаунт успешно удалён!")
        else:
            await bot.send_message(message.from_user.id, "Что-то пошло не так!")
        await state.clear()
    elif answer == "Редакторовать профиль":
        await message.answer("Выберите поле которое вы хотите изменить:", reply_markup=profile_column_keyboard)
        await state.set_state(ProfileState.change)


@dp.callback_query(ProfileState.change)
async def change_process(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    await state.set_state(ProfileState.change_process)
    await callback_query.message.delete()
    if callback_data == "name":
        await bot.send_message(callback_query.from_user.id, "Введите новое имя:")
        await state.update_data(column_name="name")
    elif callback_data == "house_number":
        await bot.send_message(callback_query.from_user.id, "Введите номер дома:")
        await state.update_data(column_name="house_number")
    elif callback_data == "apartment_number":
        await bot.send_message(callback_query.from_user.id, "Введите номер квартиры:")
        await state.update_data(column_name="apartment_number")
    elif callback_data == "entrance_number":
        await bot.send_message(callback_query.from_user.id, "Введите номер подьезда:")
        await state.update_data(column_name="entrance_number")
    elif callback_data == "floor_number":
        await bot.send_message(callback_query.from_user.id, "Введите номер этажа:")
        await state.update_data(column_name="floor_number")
    elif callback_data == "comment_to_address":
        await bot.send_message(callback_query.from_user.id, "Введите комментарии к адресу:")
        await state.update_data(column_name="comment_to_address")
    else:
        await bot.send_message(callback_query.from_user.id, "Нажмите на кнопку", reply_markup=profile_column_keyboard)
        await state.set_state(ProfileState.change)


@dp.message(ProfileState.change_process)
async def name_change_process(message: types.Message, state: FSMContext):
    new_name = message.text
    callback_context = await state.get_data()
    column_name = callback_context.get("column_name")
    context = {
        column_name: new_name
    }
    status = await user_change_column(telegram_id=message.from_user.id, data=context, token=TOKEN)
    if status == 200:
        await message.answer(f"Данные успешно изменены!", reply_markup=profile_view_keyboard)
        await state.clear()
    else:
        await message.answer("Что-то пошло не так!", reply_markup=profile_view_keyboard)
        await state.clear()


@dp.message(RegistrationStates.name)
async def process_name(message: types.Message, state: FSMContext):
    try:
        full_name = message.text.split(" ")
        await state.update_data(name=full_name[1], last_name=full_name[0], surname=full_name[2], telegram_id=message.from_user.id)
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
    except IndexError or AttributeError as e:
        await bot.send_message(message.from_user.id, "У вас неправильный формат!")
        await message.answer(f"Введи свое Ф.И.О в формате:\n\nФамилия Имя Отчество\n\nЧерез пробел!")


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
    data = await fetch_rates_data(TOKEN)

    options = [{'name': item['rate_name'], 'callback_data': str(item['id'])} for item in data]

    await send_rates(callback_query, options)

    await state.set_state(RegistrationStates.rate)


@dp.callback_query(RegistrationStates.rate)
async def callback_query_process_rate(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(rate=callback_query.data)
    await callback_query.message.delete()
    await bot.send_message(callback_query.from_user.id, "Отправьте локацию:", reply_markup=location_keyboard)
    await state.set_state(RegistrationStates.location)


@dp.message(RegistrationStates.location, F.location)
async def handle_location(message: types.Message, state: FSMContext):
    latitude = message.location.latitude
    longitude = message.location.longitude

    await state.update_data(latitude=latitude, longitude=longitude)

    message_id = await bot.send_message(message.from_user.id, """
ввидите ваш адрес в формате :

Дом/кватриру/Подьезд/Этаж

Пример: 30/16/2/1
                                        """)
    await state.update_data(message_id=message_id.message_id)
    await state.set_state(RegistrationStates.home)


@dp.message(RegistrationStates.home)
async def process_house_data(message: types.Message, state: FSMContext):
    try:
        list_data = message.text.split("/")
        
        await state.update_data(house_number=list_data[0], apartment_number=list_data[1], entrance_number=list_data[2], floor_number=list_data[3])
        await message.delete()
        
        data = await state.get_data()
        
        message_id = data.get("message_id")
        message_id = await bot.edit_message_text("Комментарии к адресу:", message.chat.id, message_id)
        
        await state.update_data(message_id=message_id.message_id)
        await state.set_state(RegistrationStates.comment)
    except IndexError or AttributeError as e:
        print(e)
        await bot.send_message(message.from_user.id, "У вас неправильный формат!")
        message_id = await bot.send_message(message.from_user.id, """
ввидите ваш адрес в формате :

Дом/кватриру/Подьезд/Этаж

Пример: 30/16/2/1
    """)
        await state.update_data(message_id=message_id.message_id)


@dp.message(RegistrationStates.comment)
async def process_comment(message: types.Message, state: FSMContext):
    await state.update_data(comment_to_address=message.text)
    await message.delete()

    context = await state.get_data()

    try:
        await post_user_info(data=context, token=TOKEN)
        
        await bot.send_message(message.from_user.id, "Спасибо за регистрацию!", reply_markup=profile_view_keyboard)
        await state.clear()
    except Exception as e:
        print(e)
        await bot.send_message(message.from_user.id, "Что-то пошло не так!", reply_markup=register_keyboard)


@dp.message(F.photo, OrderCreate.photo)
async def get_accept_photo_process(message: types.Message, state: FSMContext):
    photo_data = message.photo[-1]
    file_id = photo_data.file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path

    file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

    # Отправляем GET-запрос для загрузки файла
    response = requests.get(file_url)

    if response.status_code == 200:
        photo_dir = f"accept/photo/{message.from_user.id}.jpg"
        # Открываем файл для записи в бинарном режиме и записываем в него содержимое ответа
        with open(photo_dir, "wb") as file:
            file.write(response.content)
        user = await get_user_data(message.from_user.id, token=TOKEN)
        rate_count = int(user["rate_count"])
        if user != None:
            if rate_count < 1:
                await message.answer("У вас закончились количество заказов, количество оставших заказов - 0")
                return
            new_count = rate_count - 1
            context = {
                "client_id": message.from_user.id,
                "client_photo": photo_dir
            }
            response_code = await create_order(data=context, token=TOKEN)
            if response_code == 201:
                user_context = {
                    "rate_count": str(new_count)
                }
                response_code = await user_change_column(message.from_user.id, data=user_context, token=TOKEN)
                if response_code == 200:
                    await message.answer(f"Заказ создан - ваш остаток заказов: {new_count}", reply_markup=profile_view_keyboard)
                else:
                    await message.answer("Что-то пошло не так!", reply_markup=profile_view_keyboard)
            else:
                await message.answer("Что-то пошло не так!", reply_markup=profile_view_keyboard)
    else:
        await message.answer("Ошибка при загрузке фотографии!")
    
    await state.clear()


@dp.message()
async def registration_start(message: types.Message, state: FSMContext):
    message_answer = message.text
    user_data = await get_user_data(message.from_user.id, token=TOKEN)
    if message_answer == "Профиль":
        
        if user_data != None:
            status = "Активен🟢" if user_data["is_active"] == True else "Неактивен🔴"
            await message.answer(f"имя: {user_data['name']}\nномер телефона: {user_data['phone_number']}\nномер дома: {user_data['house_number']}\nномер квартиры: {user_data['apartment_number']}\nномер подьезда: {user_data['entrance_number']}\nэтаж: {user_data['floor_number']}\nкомментарии к адресу: {user_data['comment_to_address']}\nСтатус: {status}", reply_markup=delete_keyboard)
        else:
            await message.answer("вы ещё не регистрировались", reply_markup=register_keyboard)

    elif message_answer == "Пройти Регистрацию":
        status = await user_exist(message.from_user.id, token=TOKEN)
        if status == 200:
            await message.answer(f"Вы уже регистрировались!")
        else:
            await message.answer(f"Давай начнем процесс регистрации. Введи свое Ф.И.О в формате:\n\nФамилия Имя Отчество\n\nЧерез пробел!")
            await state.set_state(RegistrationStates.name)

    elif message_answer == "Помощь":
        await message.answer(f"link to operator @jacurlive", reply_markup=profile_view_keyboard)

    elif message_answer == "◀️Назад":
        await message.answer(f"""
Для пользования бота можете использовать следующие комманды:

/start - Для начала использования или для рестарта

Нажмите на кнопку - Профиль - для полной информации вашего аккаунта
Нажмите на кнопку - Помощь - что бы связаться с администратором
""", reply_markup=profile_view_keyboard)

    elif message_answer == "Удалить аккаунт❌":
        delete_response = await delete_user_data(message.from_user.id, token=TOKEN)
        if delete_response == 204:
            await message.delete()
            await bot.send_message(message.from_user.id, "Аккаунт успешно удалён!")
        else:
            await bot.send_message(message.from_user.id, "Что-то пошло не так!")

    elif message_answer == "Редакторовать профиль":
        await message.answer("Выберите поле которое вы хотите изменить:", reply_markup=profile_column_keyboard)
        await state.set_state(ProfileState.change)

    elif message_answer == "Создать заказ":
        order = await order_exist(message.from_user.id, token=TOKEN)
        if order == False:
            rate_count = int(user_data["rate_count"])
            if rate_count < 1:
                await message.answer("У вас закончились количество заказов, количество оставших заказов - 0", reply_markup=profile_view_keyboard)
                return
            await message.answer("Отправьте фотографию пакетов возле вашей двери, что-бы курьер мог взять именно ваш заказ")
            await state.set_state(OrderCreate.photo)
        else:
            await message.answer("У вас есть не законченный заказ, в ближайшее время наш курьер закончит ваш заказ.Если есть проблемы нажмите на кнопку Помощь", reply_markup=profile_view_keyboard)

    elif message_answer == "Актуальный заказ":
        order = await order_exist(message.from_user.id, token=TOKEN)
        if order == False:
            await message.answer("У вас ещё нет актуальных заказов, нажмите на кнопку Создать заказ", reply_markup=profile_view_keyboard)
        else:
            date = order['created_date']

            datetime_object = datetime.fromisoformat(date)

            time_only = datetime_object.strftime("%H:%M")

            status = "Закончен🟢" if order["is_completed"] == True else "Незакончен🔴"
            await message.answer(f"id: {order['id']}\nСтатус: {status}\nСтатус курьера: {order['is_taken']}\nВремя создания: {time_only}", reply_markup=profile_view_keyboard)

    else:
        await message.answer("Для полной информации введите комманду /help")


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
