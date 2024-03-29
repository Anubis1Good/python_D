from aiogram import Bot, Dispatcher, F
from basic_handler import hello_handler, error_handler, photo_handler, shout_handler, bye_handler, sum_handler
import asyncio

TOKEN = '6348032181:AAGh3nrYTBpO_03WNaNFizomgKXqlHzVJvY'

async def start():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.message.register(shout_handler, F.text.isupper())
    dp.message.register(hello_handler, F.text.lower().find('привет') != -1)
    dp.message.register(bye_handler, F.text.lower().find('пока') != -1)
    dp.message.register(sum_handler, F.text.lower().find('сложи') != -1 & F.text.lower().find('и') != -1)

    dp.message.register(photo_handler,F.photo)
    dp.message.register(error_handler)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())