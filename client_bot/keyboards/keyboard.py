from fetches.fetch import fetch_place_data, fetch_rates_data, post_user_info

from aiogram import types


contact_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Отправить контакт", request_contact=True)]],
                                     resize_keyboard=True, one_time_keyboard=True)


register_keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Пройти Регистрацию")]], resize_keyboard=True, one_time_keyboard=True)


confirm_keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text="Confirm✅", callback_data="true"), types.InlineKeyboardButton(text="Cancel❌", callback_data="false")]])

delete_keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text="Delete Account❌", callback_data="delete")]])

async def send_place(chat_id, options):
    kb = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text=item['name'], callback_data=item['callback_data'])] for item in options]) # one line button one item 

    await bot.send_message(chat_id, "Выберите район:", reply_markup=kb)


async def send_rates(chat_id, options):
    kb = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text=item['name'], callback_data=item['callback_data'])] for item in options], row_width=1)

    await bot.send_message(chat_id, "Выберите тариф:", reply_markup=kb)
