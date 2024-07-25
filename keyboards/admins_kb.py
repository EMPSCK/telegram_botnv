from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


cancel_button = [InlineKeyboardButton(text="Отменить операцию", callback_data='cancel_load')]
load_judges_kb = InlineKeyboardMarkup(inline_keyboard=[cancel_button])

menu_button_1 = [InlineKeyboardButton(text='Создать турнир', callback_data='create_competition')]
menu_button_2 = [InlineKeyboardButton(text='Редактировать турнир', callback_data='edit_competition')]
menu_kb = InlineKeyboardMarkup(inline_keyboard=[menu_button_1, menu_button_2])
