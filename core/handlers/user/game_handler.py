from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from core.states.states import PlayerRegistrationState as PRS
from core.keyboards.inline.game_keyboards import get_inline_race, get_inline_class
from core.db.utils.json_scripts import save_character, load_character

router = Router(name=__name__)

@router.message(Command(commands='form'))
async def get_form_handler(msg: Message, state: FSMContext):
    await msg.answer('Добро пожаловать в форму регистрации.\nВведите имя вашего персонажа: ')
    await state.set_state(PRS.hero_name)

@router.message(PRS.hero_name)
async def get_name_handler(msg: Message, state: FSMContext):
    await msg.answer(f'Ваше имя {msg.text}.',reply_markup=get_inline_race())
    await state.update_data(hero_name=msg.text)
    await state.set_state(PRS.hero_race)

@router.callback_query(PRS.hero_race)
async def get_race_handler(call:CallbackQuery, state: FSMContext):
    await call.message.answer(f'Ваша раса {call.data}.',reply_markup=get_inline_class())
    await state.update_data(hero_race=call.data)
    await state.set_state(PRS.hero_class)
    await call.answer()

@router.callback_query(PRS.hero_class)
async def get_class_handler(call:CallbackQuery, state: FSMContext):
    await call.message.answer('Загрузите фото вашего персонажа: ')
    await state.update_data(hero_class=call.data)
    await state.set_state(PRS.hero_avatar)
    await call.answer()

@router.message(PRS.hero_avatar)
async def get_avatar_handler(msg: Message, state: FSMContext):
    try:
        file = msg.photo[-1].file_id
        await state.update_data(hero_avatar=file)
        data = await state.get_data()
        save_character(file,data)
        await msg.answer_photo(
            photo=file,
            caption=f'Поздравляем вами создан <i>{data["hero_race"]} {data["hero_class"]}</i> по имени <b>{data["hero_name"]}</b> 🫵👍'
            )
        await state.clear()
    except:
        await msg.answer('Нет фото. Загрузите фото вашего персонажа: ')
        
@router.message(Command(commands='character'))
async def get_my_char_handler(msg:Message):
    try:
        data = load_character(msg.from_user.id)
        await msg.answer_photo(
            photo=data['hero_avatar'],
            caption=f'Ваш персонаж <i>{data["hero_race"]} {data["hero_class"]}</i> по имени <b>{data["hero_name"]}</b> 🫵👍'
        )
    except:
        await msg.answer('Кажется у вас нет персонажа')

