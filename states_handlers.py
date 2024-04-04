from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import WorkState

async def off_handler(msg: Message, state: FSMContext):
    await msg.answer('Бот отключен. Для запуска бота введите команду /on')
    await state.set_state(WorkState.OFF)

async def sleep_handler(msg: Message, state: FSMContext):
    await msg.answer('Бот отключен. Для запуска бота введите команду /on')

async def on_handler(msg: Message, state: FSMContext):
    await msg.answer('Бот включен!')
    await state.clear()

