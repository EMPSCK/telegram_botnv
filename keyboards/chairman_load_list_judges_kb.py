from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

cancel_button = [InlineKeyboardButton(text="Отменить операцию", callback_data='cancel_load')]
load_judges_kb = InlineKeyboardMarkup(inline_keyboard=[cancel_button])
