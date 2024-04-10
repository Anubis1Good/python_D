from aiogram import Bot, Router
from aiogram.types import CallbackQuery

router = Router(name=__name__)

async def select_game(call: CallbackQuery, bot: Bot):
    await call.message.answer(text=f"{call.data} - это отличный выбор!")
    await call.answer()

router.callback_query.register(select_game)


