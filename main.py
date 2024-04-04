from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from commands import set_commands
from basic_handler import hello_handler, error_handler, photo_handler, shout_handler, bye_handler, sum_handler,start_handler, game_menu_handler
from callback_handler import select_game
from states_handlers import on_handler,off_handler,sleep_handler
from game_handler import *
from states import WorkState, PlayerRegistrationState as PRS
import asyncio

TOKEN = '6348032181:AAGh3nrYTBpO_03WNaNFizomgKXqlHzVJvY'

async def start():
    bot = Bot(token=TOKEN,parse_mode='HTML')
    dp = Dispatcher()
    
    dp.startup.register(set_commands)

    dp.message.register(on_handler, WorkState.OFF, Command(commands='on'))
    dp.message.register(sleep_handler, WorkState.OFF)
    dp.message.register(off_handler,Command(commands='off'))

    dp.message.register(get_form_handler, Command(commands='form'))
    dp.message.register(get_name_handler, PRS.hero_name)
    dp.callback_query.register(get_race_handler, PRS.hero_race)
    dp.callback_query.register(get_class_handler, PRS.hero_class)
    dp.message.register(get_avatar_handler, PRS.hero_avatar)

    dp.message.register(get_my_char_handler,Command(commands='character'))
    dp.message.register(start_handler, Command(commands=['start']))
    dp.message.register(game_menu_handler, Command(commands=['games']))

    dp.message.register(shout_handler, F.text.isupper())
    dp.message.register(hello_handler, F.text.lower().find('привет') != -1)
    dp.message.register(bye_handler, F.text.lower().find('пока') != -1)
    dp.message.register(sum_handler, F.text.lower().find('сложи') != -1 & F.text.lower().find('и') != -1)

    dp.message.register(photo_handler,F.photo)
    dp.message.register(error_handler)

    dp.callback_query.register(select_game)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())