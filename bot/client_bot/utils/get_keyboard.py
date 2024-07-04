from utils.translation.localization import get_localized_message
from keyboards.keyboard import profile_column_keyboard, profile_view_keyboard


async def get_profile_view_btn(language_code):
    localized_btn_1 = await get_localized_message(language_code, "profile_btn")
    localized_btn_2 = await get_localized_message(language_code, "create_order_btn")
    localized_btn_3 = await get_localized_message(language_code, "actual_order_btn")
    localized_btn_4 = await get_localized_message(language_code, "change_language_btn")
    localized_btn_5 = await get_localized_message(language_code, "help_btn")
    profile_btn = await profile_view_keyboard(localized_btn_1, localized_btn_2, localized_btn_3, localized_btn_4,
                                              localized_btn_5)

    return profile_btn


async def get_profile_column(language_code):
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
    
    return profile_column_btn