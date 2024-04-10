from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_inline_race():
    kb = InlineKeyboardBuilder()
    kb.button(text='Человек👨',callback_data='человек')
    kb.button(text='Эльф🧝',callback_data='эльф')
    kb.button(text='Орк🗿',callback_data='орк')
    kb.button(text='Гном🧌',callback_data='гном')
    return kb.as_markup()


def get_inline_class():
    kb = InlineKeyboardBuilder()
    kb.button(text='Танк🛡️',callback_data='танк')
    kb.button(text='Боец⚔️',callback_data='боец')
    kb.button(text='Лекарь🍀',callback_data='лекарь')
    kb.button(text='Маг🪬',callback_data='маг')
    return kb.as_markup()



