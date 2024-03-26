from aiogram import types


contact_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Отправить контакт", request_contact=True)]],
                                     resize_keyboard=True, one_time_keyboard=True)

location_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Отправить локацию", request_location=True)]], resize_keyboard=True, one_time_keyboard=True)

register_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Пройти Регистрацию")]], resize_keyboard=True, one_time_keyboard=True)

confirm_keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text="Confirm✅", callback_data="true"), types.InlineKeyboardButton(text="Cancel❌", callback_data="false")]])

profile_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Профиль")]], resize_keyboard=True, one_time_keyboard=True)

delete_kb = [
    [types.KeyboardButton(text="Delete Account❌")],
    [types.KeyboardButton(text="Изменить имя")],
    [types.KeyboardButton(text="Изменить номер телефона")],
    [types.KeyboardButton(text="Изменить номер дома")],
    [types.KeyboardButton(text="Изменить номер квартиры")],
    [types.KeyboardButton(text="Изменить номер подьезда")],
    [types.KeyboardButton(text="Изменить этаж")],
    [types.KeyboardButton(text="Изменить комментарии к адресу")]
]

delete_keyboard = types.ReplyKeyboardMarkup(keyboard=delete_kb, resize_keyboard=True, one_time_keyboard=True)
