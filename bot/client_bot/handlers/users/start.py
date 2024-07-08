import logging

from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram import types

from utils.translation.localization import get_localized_message
from utils.get_keyboard import get_profile_view_btn
from data import config
from keyboards.keyboard import language_keyboard
from states.state import RegistrationStates
from loader import dp, bot
from utils.fetch import (
    get_user_data,
    user_language,
    get_customers
)


TOKEN = config.TOKEN


# @dp.message(CommandStart())
async def start_command(message: types.Message, state: FSMContext):
    # user_data = await get_user_data(message.from_user.id, token=TOKEN)

    # if user_data is not None:
    #     await message.answer("Registered")
    # else:
    #     contact_btn = await contact_keyboard('contact')
    #     await message.answer("NOT registered", reply_markup=contact_btn)
    #     await state.set_state(TelegramIDPut.phone)


    #  ------------- V1 -----------------
    user_data = await get_user_data(message.from_user.id, token=TOKEN)

    if user_data is not None:
        user_id = message.from_user.id
        language_data = await user_language(user_id=user_id, token=TOKEN)
        language_code = language_data['lang']

        localized_message = await get_localized_message(language_code, "greeting_registered")

        profile_btn = await get_profile_view_btn(language_code=language_code)
        await message.answer(localized_message, reply_markup=profile_btn)
        await state.clear()
    else:
        language_btn = await language_keyboard()
        welcome_message = await get_localized_message("none", "welcome")
        await message.answer(welcome_message, reply_markup=language_btn)
        await state.set_state(RegistrationStates.get_language)


@dp.message(Command("message"))
async def message_to_all(message: types.Message):
    user_id = message.from_user.id

    if user_id == 5812918934:
        text = message.text[8:]
        data = await get_customers(token=TOKEN)
        for user in data:
            try:
                await bot.send_message(user['telegram_id'], text)
                print(user['telegram_id'])
            except Exception as ex:
                logging.error(ex)

print(123)
