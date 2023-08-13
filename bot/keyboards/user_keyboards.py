from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def get_main_ikb() -> InlineKeyboardMarkup:
    """Get main ikb
    """
    
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text = '/help', message = '/help', callback_data='cb_helpbtn')]
    ])
    

    return ikb


def get_main_kb() -> ReplyKeyboardMarkup:
    """Get main kb
    """

    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add('Помощь 🔎')
    kb.add('Бот 📗')

    return kb