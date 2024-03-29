from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Кнопка 1')
    keyboard_builder.button(text='Кнопка 2')
    keyboard_builder.button(text='Отправить геолокацию', request_location=True)
    keyboard_builder.button(text='Отправить свой контакт',request_contact=True)
    keyboard_builder.adjust(2,1,1)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder='Нажмите кнопку'
    )