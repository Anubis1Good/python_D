from aiogram import Router
from aiogram.types import Message

router = Router(name=__name__)

@router.message()
async def error_handler(msg: Message):
    await msg.answer(text=f'Мне нечего ответить')