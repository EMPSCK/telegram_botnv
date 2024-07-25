from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from queries import get_scrutinner_active_comp_query


def gen_list_comp(tg_id):
    list_comp_buttons = []

    competitions = get_scrutinner_active_comp_query.get_list_comp(tg_id)
    for comp in competitions:
        list_comp_buttons.append([InlineKeyboardButton(text=comp['compName'], callback_data=f"Scomp_{comp['compId']}")])
    list_comp_buttons.append([InlineKeyboardButton(text='Вернуться к меню', callback_data='back_to_scrutineer_menu')])
    return InlineKeyboardMarkup(inline_keyboard=list_comp_buttons)
