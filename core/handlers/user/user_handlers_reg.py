from core.handlers.user.basic_handler import *
from core.handlers.user.callback_handler import *
from core.handlers.user.game_handler import *
from core.handlers.user.states_handlers import *
from aiogram import Dispatcher
from aiogram.filters import Command


def registration_user_handlers(dp: Dispatcher):
    dp.message.register(on_handler, WorkState.OFF, Command(commands='on'))
    dp.message.register(sleep_handler, WorkState.OFF)
    dp.message.register(off_handler,Command(commands='off'))