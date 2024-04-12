from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),
        BotCommand(
            command='cancel',
            description='Сбросить'
        ),
        BotCommand(
            command='games',
            description='Игры'
        ),
        BotCommand(
            command='on',
            description='включить бота'
        ),
        BotCommand(
            command='off',
            description='отключить бота'
        ),
        BotCommand(
            command='form',
            description='Создать персонажа'
        ),
        BotCommand(
            command='character',
            description='Показать моего персонажа'
        ),
        BotCommand(
            command='low_price',
            description='Показать дешевые товары'
        ),
        BotCommand(
            command='high_price',
            description='Показать дорогие товары'
        ),



    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())