from aiogram import Bot
from aiogram.types import CallbackQuery


async def select_game(call: CallbackQuery, bot: Bot):
    await call.message.answer(text=f"{call.data} - это отличный выбор!")
    await call.answer()




