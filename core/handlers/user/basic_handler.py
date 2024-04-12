from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from core.keyboards.reply.reply_keyboards import get_reply_keyboard
from core.keyboards.inline.inline_keyboards import get_inline_keyboard
from core.filters.is_contact import IsTrueContact

router = Router(name=__name__)

@router.message(Command(commands='start'))
async def start_handler(msg: Message):
    await msg.answer(text="Hello! I'm bot!", reply_markup=get_reply_keyboard())

@router.message(F.text.lower().find('привет') != -1)
async def hello_handler(msg: Message):
    await msg.answer(text=f'Привет! {msg.from_user.first_name}')

@router.message(F.text.lower().find('пока') != -1)
async def bye_handler(msg: Message):
    await msg.answer(text=f'Пока! {msg.from_user.first_name}')

@router.message(F.photo)
async def photo_handler(msg: Message):
    await msg.reply('Классное фото!')

@router.message(F.text.lower().find('сложи') != -1, F.text.lower().find('и') != -1)
async def sum_handler(msg: Message):
    result = 'Нет результата!'
    try:
        data = msg.text.split()
        num1 = int(data[1])
        num2 = int(data[3])
        result = num1+ num2
    finally:
        await msg.reply(text=f'{result}')

@router.message(F.text.isupper())
async def shout_handler(msg: Message):
    await msg.reply(text=f'Пожалуйста, не кричите.')

@router.message(Command(commands='games'))
async def game_menu_handler(msg: Message):
    await msg.answer(text='Меню', reply_markup=get_inline_keyboard())

@router.message(F.contact, IsTrueContact())
async def get_true_contact(msg:Message):
    await msg.answer('Вы прислали свой контакт.')

@router.message(F.contact)
async def get_fake_contact(msg:Message):
    await msg.answer('Вы прислали не свой контакт.')


    