from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_inline_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text='Warcraft',callback_data='World of Warcraft')
    kb.button(text='Diablo',callback_data='Diablo III')
    kb.button(text='Starcraft',callback_data='Startcraft II')
    kb.button(text='HOTS',callback_data='Heroes of the storm')
    kb.button(text='Hearthstone',callback_data='Hearthstone')
    kb.button(text='Overwatch',callback_data='Overwatch 2')
    kb.button(text='Blizzard',url='https://www.blizzard.com/ru-ru/')
    kb.adjust(3,3,1)
    return kb.as_markup()