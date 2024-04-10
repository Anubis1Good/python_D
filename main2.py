import asyncio
from aiogram import Bot, Dispatcher
from core.utils.commands import set_commands
from core.handlers.all_routers import all_routers

TOKEN = '6348032181:AAGh3nrYTBpO_03WNaNFizomgKXqlHzVJvY'

async def start():
    bot = Bot(token=TOKEN,parse_mode='HTML')
    dp = Dispatcher()

    for router in all_routers:
        dp.include_router(router)
    
    dp.startup.register(set_commands)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())


    