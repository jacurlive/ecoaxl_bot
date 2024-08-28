from aiogram import types


async def payment_type_keyboard(text_1, text_2):
    payment_type_kb = [
        [
            types.KeyboardButton(
                text=text_1
            ),
            types.KeyboardButton(
                text=text_2
            )
        ]
    ]

    payment_type_k = types.ReplyKeyboardMarkup(keyboard=payment_type_kb, resize_keyboard=True, one_time_keyboard=True)
    return payment_type_k


async def register_type_keyboard(text_1: str, text_2: str):
    register_type_kb = [
        [
            types.KeyboardButton(
                text=text_1
                ),
            types.KeyboardButton(
                text=text_2
            )
        ]
    ]

    register_type_k = types.ReplyKeyboardMarkup(keyboard=register_type_kb, resize_keyboard=True, one_time_keyboard=True)

    return register_type_k


async def contact_keyboard(text):
    contact_k = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text=text, request_contact=True)]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return contact_k


async def location_keyboard(text):
    location_k = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text=text, request_location=True)]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return location_k


async def register_keyboard(text_1: str, text_2: str):
    register_kb = [
        [
            types.KeyboardButton(text=text_1),
            types.KeyboardButton(text=text_2)
        ]
    ]

    register_k = types.ReplyKeyboardMarkup(
        keyboard=register_kb,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return register_k


async def language_keyboard():
    language_kb = [
        [
            types.InlineKeyboardButton(text="ru", callback_data="ru"),
            types.InlineKeyboardButton(text="uz", callback_data="uz")
        ]
    ]

    language_k = types.InlineKeyboardMarkup(inline_keyboard=language_kb)

    return language_k


async def confirm_keyboard(text_1, text_2):
    confirm_k = types.InlineKeyboardMarkup(
        inline_keyboard=[[types.InlineKeyboardButton(text=text_1, callback_data="true"),
                          types.InlineKeyboardButton(text=text_2, callback_data="false")]]
    )

    return confirm_k


async def profile_view_keyboard(text_1, text_2, text_3, text_4, text_5, text_6):
    profile_view_kb = [
        [
            types.KeyboardButton(text=text_1),
            types.KeyboardButton(text=text_2),
            types.KeyboardButton(text=text_3)
        ],
        [
            types.KeyboardButton(text=text_4),
            types.KeyboardButton(text=text_5),
            types.KeyboardButton(text=text_6)
        ]
    ]

    profile_view_k = types.ReplyKeyboardMarkup(
        keyboard=profile_view_kb,
        resize_keyboard=True,
        one_time_keyboard=True
    )

    return profile_view_k


async def delete_keyboard(text_1, text_2, text_3):
    delete_kb = [
        [
            types.KeyboardButton(text=text_1),
            types.KeyboardButton(text=text_2)
        ],
        [
            types.KeyboardButton(text=text_3)
        ]
    ]

    delete_k = types.ReplyKeyboardMarkup(
        keyboard=delete_kb,
        resize_keyboard=True,
        one_time_keyboard=True
    )

    return delete_k


async def profile_column_keyboard(text_1, text_2, text_3, text_4, text_5, text_6):
    profile_column_kb = [
        [
            types.InlineKeyboardButton(text=text_1, callback_data="name"),
            types.InlineKeyboardButton(text=text_2, callback_data="house_number"),
            types.InlineKeyboardButton(text=text_3, callback_data="apartment_number"),
        ],
        [
            types.InlineKeyboardButton(text=text_4, callback_data="entrance_number"),
            types.InlineKeyboardButton(text=text_5, callback_data="floor_number"),
            types.InlineKeyboardButton(text=text_6, callback_data="comment_to_address")
        ]
    ]

    profile_column_k = types.InlineKeyboardMarkup(
        inline_keyboard=profile_column_kb
    )

    return profile_column_k


async def additions_keyboard(text_1, text_2):
    additions_kb = [
        [
            types.KeyboardButton(text=text_1),
            types.KeyboardButton(text=text_2)
        ]
    ]
    additions_k = types.ReplyKeyboardMarkup(keyboard=additions_kb, resize_keyboard=True)

    return additions_k
