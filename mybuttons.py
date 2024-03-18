from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

menu = ReplyKeyboardMarkup(
    keyboard= [

    [KeyboardButton(text="/news"),
    KeyboardButton(text="Admin bilan bog'lanish"),],

    

    ],
    resize_keyboard=True
    
    
)

keyingi = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="keyingisi", callback_data="keyingisi")]
        
        
    ]
    
    
    
)