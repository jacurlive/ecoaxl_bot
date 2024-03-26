from aiogram import types


contact_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Отправить контакт", request_contact=True)]],
                                     resize_keyboard=True, one_time_keyboard=True)

location_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Отправить локацию", request_location=True)]], resize_keyboard=True, one_time_keyboard=True)

register_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Пройти Регистрацию")]], resize_keyboard=True, one_time_keyboard=True)

confirm_keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text="Confirm✅", callback_data="true"), types.InlineKeyboardButton(text="Cancel❌", callback_data="false")]])

delete_keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text="Delete Account❌", callback_data="delete")], [types.InlineKeyboardButton(text="Изменить имя", callback_data="name")]])

profile_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Профиль")]], resize_keyboard=True, one_time_keyboard=True)
