from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.states.states import WorkState
from aiogram.filters import Command

router = Router(name=__name__)

@router.message(Command(commands='off'))
async def off_handler(msg: Message, state: FSMContext):
    await msg.answer('Бот отключен. Для запуска бота введите команду /on')
    await state.set_state(WorkState.OFF)

@router.message(WorkState.OFF)
async def sleep_handler(msg: Message, state: FSMContext):
    await msg.answer('Бот отключен. Для запуска бота введите команду /on')

@router.message(WorkState.OFF, Command(commands='on'))
async def on_handler(msg: Message, state: FSMContext):
    await msg.answer('Бот включен!')
    await state.clear()

