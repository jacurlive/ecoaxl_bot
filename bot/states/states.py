from aiogram.filters.state import StatesGroup, State


class RegistrationStates(StatesGroup):
    name = State()
    phone_number = State()
    confirmation = State()
    place = State()
    rate = State()
    location = State()
    