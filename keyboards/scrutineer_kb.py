from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from queries import scrutineer_queries

def gen_list_comp(tg_id):
    list_comp_buttons = []

    competitions = scrutineer_queries.get_list_comp(tg_id)
    for comp in competitions:
        list_comp_buttons.append([InlineKeyboardButton(text=comp['compName'], callback_data=f"Scomp_{comp['compId']}")])
    list_comp_buttons.append([InlineKeyboardButton(text='Вернуться к меню', callback_data='back_to_scrutineer_menu')])
    return InlineKeyboardMarkup(inline_keyboard=list_comp_buttons)

menu_button = [InlineKeyboardButton(text='Задать активное соревнование', callback_data='set_active_competition_for_S')]
menu_kb = InlineKeyboardMarkup(inline_keyboard=[menu_button])
