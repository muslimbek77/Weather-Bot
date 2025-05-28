from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# viloyatlar_btn = ReplyKeyboardMarkup(
#     keyboard=
#     [
#         # [KeyboardButton(text="Toshkent"), KeyboardButton(text="Andijon")],
#         [KeyboardButton(text="Contact yuborish",request_contact=True)],
#         [KeyboardButton(text="Manzilni yuborish",request_location=True)], 
#     ],
#     resize_keyboard=True,
#     input_field_placeholder="Viloyatni tanlang..."
#     )
city = {
    "Toshkent": "tashkent",
    "Andijon": "andyzhan",
    "Farg'ona": "ferhana",
    "Namangan": "namanhan",
    "Samarqand": "samarkand",
    "Buxoro": "bukhara",
    "Navoiy": "navoi",
    "Qashqadaryo": "karshi",  # Qarshi shahri
    "Surxondaryo": "termez",  # Termiz shahri
    "Xorazm": "urhench",      # Urganch shahri
    "Qoraqalpog‘iston": "nukus",
    "Jizzax": "dzhyzak",
    "Sirdaryo": "hulistan",
}
viloyatlar_btn = ReplyKeyboardBuilder()
for region in city.keys():
    viloyatlar_btn.add(KeyboardButton(text=region)) 
viloyatlar_btn.adjust(1,2)
