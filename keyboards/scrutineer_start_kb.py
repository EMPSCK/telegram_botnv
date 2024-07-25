from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_button = [InlineKeyboardButton(text='Задать активное соревнование', callback_data='set_active_competition_for_S')]
menu_kb = InlineKeyboardMarkup(inline_keyboard=[menu_button])
