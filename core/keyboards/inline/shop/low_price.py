from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.models.product import LowPriceProduct

def get_low_price_kb():
    kb = InlineKeyboardBuilder()
    kb.button(
        text='Попсокет',
        callback_data=LowPriceProduct(
            name='Попсокет',
            price=100,
            lucky_sale=True)
        )
    kb.button(text='Линейка-головоломка',callback_data=LowPriceProduct(name='Линейка-головоломка',price=150,lucky_sale=True))
    kb.button(text='Пенал',callback_data=LowPriceProduct(name='Пенал',price=500,lucky_sale=True))
    kb.button(text='Наушники с ушками',callback_data=LowPriceProduct(name='Наушники с ушками',price=600,lucky_sale=False))
    kb.button(text='Коврик для мыши',callback_data=LowPriceProduct(name='Коврик для мыши',price=600,lucky_sale=False))
    kb.button(text='Мармеладские игры',callback_data=LowPriceProduct(name='Мармеладские игры',price=600,lucky_sale=True))
    kb.button(text='Алголавка',url='https://algolavka.tilda.ws/algolavka')
    kb.adjust(3,3,1)
    return kb.as_markup()