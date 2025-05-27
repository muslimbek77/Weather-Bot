from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

viloyatlar_btn = ReplyKeyboardMarkup(
    keyboard=
    [
        [KeyboardButton(text="Toshkent"),KeyboardButton(text="Andijon")],
        
    ],
    resize_keyboard=True,
    input_field_placeholder="Viloyatni tanlang..."
    )

