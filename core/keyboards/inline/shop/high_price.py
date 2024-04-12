from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.models.product import HighPriceProduct

def get_high_price_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text='Беспроводная клавиатура',callback_data=HighPriceProduct(name='Беспроводная клавиатура',price=2500))
    kb.button(text='Проводная Клавиатура',callback_data=HighPriceProduct(name='Проводная Клавиатура',price=2200))
    kb.button(text='Шоппер',callback_data=HighPriceProduct(name='Шоппер',price=2000))
    kb.button(text='Настольная лампа',callback_data=HighPriceProduct(name='Настольная лампа',price=1700))
    kb.button(text='Powerbank',callback_data=HighPriceProduct(name='Powerbank',price=1600))
    kb.button(text='Термос',callback_data=HighPriceProduct(name='Термос',price=1500))
    kb.button(text='Алголавка',url='https://algolavka.tilda.ws/algolavka')
    kb.adjust(3,3,1)
    return kb.as_markup()