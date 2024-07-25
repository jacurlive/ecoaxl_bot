from aiogram.filters.state import StatesGroup, State


class RegistrationStates(StatesGroup):
    get_language = State()
    name = State()
    phone_number = State()
    confirmation = State()
    place = State()
    rate = State()
    invoce = State()
    payment = State()
    location = State()
    home = State()
    comment = State()


class ProfileState(StatesGroup):
    profile = State()
    vision = State()
    change = State()
    change_process = State()


class DefaultState(StatesGroup):
    main = State()


class OrderCreate(StatesGroup):
    additions = State()
    photo = State()
    comment = State()
    accept = State()


class LanguageChange(StatesGroup):
    change = State()


class TelegramIDPut(StatesGroup):
    phone = State()


class RegisterType(StatesGroup):
    choose = State()


class Rates(StatesGroup):
    pass
