from aiogram.filters.state import StatesGroup, State


class RegistrationStates(StatesGroup):
    name = State()
    phone_number = State()
    confirmation = State()
    place = State()
    rate = State()
    location = State()
    home = State()
    comment = State()


class ProfileState(StatesGroup):
    profile = State()
    vision = State()
    name = State()


class DefaultState(StatesGroup):
    start = State()
