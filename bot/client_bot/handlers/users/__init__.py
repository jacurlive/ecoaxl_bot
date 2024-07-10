from aiogram import Router
from aiogram.filters import CommandStart, StateFilter

from . import start


def prepare_router() -> Router:
    user_router = Router()

    user_router.message.register(start.start_command, CommandStart())

    return user_router
