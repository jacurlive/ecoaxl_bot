from aiogram import types


contact_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Отправить контакт", request_contact=True)]],
                                     resize_keyboard=True, one_time_keyboard=True)

location_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Отправить локацию", request_location=True)]], resize_keyboard=True, one_time_keyboard=True)

register_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Пройти Регистрацию")]], resize_keyboard=True, one_time_keyboard=True)

confirm_keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text="Confirm✅", callback_data="true"), types.InlineKeyboardButton(text="Cancel❌", callback_data="false")]])

profile_view_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Профиль")]], resize_keyboard=True, one_time_keyboard=True)

delete_kb = [
    [
        types.KeyboardButton(text="Удалить аккаунт❌"),
        types.KeyboardButton(text="Редакторовать профиль")
    ]
]

delete_keyboard = types.ReplyKeyboardMarkup(keyboard=delete_kb, resize_keyboard=True, one_time_keyboard=True)

profile_column_kb = [
    [
        types.InlineKeyboardButton(text="Имя", callback_data="name"),
        types.InlineKeyboardButton(text="номер телефона", callback_data="phone_number"),
        types.InlineKeyboardButton(text="номер дома", callback_data="house_number")
    ],
    [
        types.InlineKeyboardButton(text="номер квартиры", callback_data="apartment_number"),
        types.InlineKeyboardButton(text="номер подьезда", callback_data="entrance_number"),
        types.InlineKeyboardButton(text="этаж", callback_data="floor_number")
    ],
    [
        types.InlineKeyboardButton(text="комментарии к адресу", callback_data="comment_to_address")
    ]
]

profile_column_keyboard = types.InlineKeyboardMarkup(inline_keyboard=profile_column_kb)