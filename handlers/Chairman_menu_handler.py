from aiogram import Router, F
from aiogram import types
from keyboards import chairmans_kb
from queries import chairman_queries
from queries import get_user_status_query
from queries import general_queries
router = Router()


#Вернуться в меню
@router.callback_query(F.data == 'back_to_chairman_menu')
async def cmd_start(call: types.CallbackQuery):
    user_status = await get_user_status_query.get_user_status(call.from_user.id)
    if user_status == 3:
        active_comp = await general_queries.get_CompId(call.from_user.id)
        comp_name = await general_queries.CompId_to_name(active_comp)
        text = f'👋Добро пожаловать в chairman интерфейс бота SS6\n\n /judges - отправить список судей\nАктивное соревнование: {comp_name}'
        await call.message.edit_text(text=text, reply_markup=chairmans_kb.menu_kb)


#Выбрать активное соревнование
@router.callback_query(F.data == 'set_active_competition')
async def cmd_start(call: types.CallbackQuery):
    user_status = await get_user_status_query.get_user_status(call.from_user.id)
    if user_status == 3:
        markup = chairmans_kb.gen_list_comp(call.from_user.id)
        await call.message.edit_reply_markup(reply_markup=markup)


#Обработка после выбора активного соревнования
@router.callback_query(F.data.startswith('comp_'))
async def cmd_start(call: types.CallbackQuery):
    user_status = await get_user_status_query.get_user_status(call.from_user.id)
    if user_status == 3:
        compId = int(call.data.replace('comp_', ''))
        await chairman_queries.set_active_comp_for_chairman(call.from_user.id, compId)
        await call.message.answer('Действие обработано')
