import asyncio
from aiogram import Bot, Dispatcher
from core.utils.commands import set_commands
from core.handlers.all_routers import all_routers
from core.utils.settings import settings

async def start():
    bot = Bot(token=settings.bot_token, parse_mode='HTML')
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