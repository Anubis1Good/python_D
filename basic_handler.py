from aiogram import Bot
from aiogram.types import Message
from reply_keyboards import get_reply_keyboard
from inline_keyboards import get_inline_keyboard

async def start_handler(msg: Message, bot: Bot):
    await msg.answer(text="Hello! I'm bot!", reply_markup=get_reply_keyboard())

async def hello_handler(msg: Message, bot: Bot):
    await msg.answer(text=f'Привет! {msg.from_user.first_name}')

async def bye_handler(msg: Message, bot: Bot):
    await msg.answer(text=f'Пока! {msg.from_user.first_name}')

async def error_handler(msg: Message, bot: Bot):
    await msg.answer(text=f'Мне нечего ответить')

async def photo_handler(msg: Message, bot: Bot):
    await msg.reply('Классное фото!')

async def sum_handler(msg: Message, bot: Bot):
    result = 'Нет результата!'
    try:
        data = msg.text.split()
        num1 = int(data[1])
        num2 = int(data[3])
        result = num1+ num2
    finally:
        await msg.reply(text=f'{result}')

async def shout_handler(msg: Message, bot: Bot):
    await msg.reply(text=f'Пожалуйста, не кричите.')


async def game_menu_handler(msg: Message, bot: Bot):
    await msg.answer(text='Меню', reply_markup=get_inline_keyboard())

