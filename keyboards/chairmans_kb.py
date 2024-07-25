from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from queries import chairman_queries

def gen_list_comp(tg_id):
    list_comp_buttons = []

    competitions = chairman_queries.get_list_comp(tg_id)
    for comp in competitions:
        list_comp_buttons.append([InlineKeyboardButton(text=comp['compName'], callback_data=f"comp_{comp['compId']}")])
    list_comp_buttons.append([InlineKeyboardButton(text='Вернуться к меню', callback_data='back_to_chairman_menu')])
    return InlineKeyboardMarkup(inline_keyboard=list_comp_buttons)

cancel_button = [InlineKeyboardButton(text="Отменить операцию", callback_data='cancel_load')]
load_judges_kb = InlineKeyboardMarkup(inline_keyboard=[cancel_button])

menu_button = [InlineKeyboardButton(text='Задать активное соревнование', callback_data='set_active_competition')]
menu_kb = InlineKeyboardMarkup(inline_keyboard=[menu_button])
