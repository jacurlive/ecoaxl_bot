from aiogram.filters.state import StatesGroup, State


class RegistrationStates(StatesGroup):
    name = State()
    phone_number = State()
    confirmation = State()
    place = State()


class ProfileState(StatesGroup):
    profile = State()
    vision = State()
    change = State()
    change_process = State()


class DefaultState(StatesGroup):
    main = State()