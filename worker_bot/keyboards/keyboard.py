from aiogram import types


contact_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Отправить контакт", request_contact=True)]],
                                     resize_keyboard=True, one_time_keyboard=True)

location_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Отправить локацию", request_location=True)]], resize_keyboard=True, one_time_keyboard=True)

register_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Пройти Регистрацию")], [types.KeyboardButton(text="Помощь")]], resize_keyboard=True, one_time_keyboard=True)

confirm_keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text="Confirm✅", callback_data="true"), types.InlineKeyboardButton(text="Cancel❌", callback_data="false")]])

profile_view_kb = [
    [
        types.KeyboardButton(text="Профиль"),
        types.KeyboardButton(text="Взять заказ")
    ],
    [
        types.KeyboardButton(text="Помощь")
    ]
]

profile_view_keyboard = types.ReplyKeyboardMarkup(keyboard=profile_view_kb, resize_keyboard=True, one_time_keyboard=True)

delete_kb = [
    [
        types.KeyboardButton(text="Удалить аккаунт❌"),
        types.KeyboardButton(text="Редакторовать профиль")
    ],
    [
        types.KeyboardButton(text="◀️Назад")
    ]
]

delete_keyboard = types.ReplyKeyboardMarkup(keyboard=delete_kb, resize_keyboard=True, one_time_keyboard=True)

profile_column_kb = [
    [
        types.InlineKeyboardButton(text="Имя", callback_data="name"),
        types.InlineKeyboardButton(text="Фамилия", callback_data="last_name"),
        types.InlineKeyboardButton(text="Отчество", callback_data="surname"),
    ]
]

profile_column_keyboard = types.InlineKeyboardMarkup(inline_keyboard=profile_column_kb)
