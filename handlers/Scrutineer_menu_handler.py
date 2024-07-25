from aiogram import Router, F
from aiogram import types
from keyboards import scrutineer_kb
from queries import get_user_status_query
from queries import chairman_queries
router = Router()


#Вернуться в меню
@router.callback_query(F.data == 'back_to_scrutineer_menu')
async def cmd_start(call: types.CallbackQuery):
    user_status = await get_user_status_query.get_user_status(call.from_user.id)
    if user_status == 2:
        text = '👋Добро пожаловать в chairman интерфейс бота SS6\n\n /judges - отправить список судий'
        await call.message.edit_text(text=text, reply_markup=scrutineer_kb.menu_kb)


#Выбрать активное соревнование
@router.callback_query(F.data == 'set_active_competition_for_S')
async def cmd_start(call: types.CallbackQuery):
    user_status = await get_user_status_query.get_user_status(call.from_user.id)
    if user_status == 2:
        markup = scrutineer_kb.gen_list_comp(call.from_user.id)
        await call.message.edit_reply_markup(reply_markup=markup)


#Обработка после выбора активного соревнования
@router.callback_query(F.data.startswith('Scomp_'))
async def cmd_start(call: types.CallbackQuery):
    user_status = await get_user_status_query.get_user_status(call.from_user.id)
    if user_status == 2:
        compId = int(call.data.replace('Scomp_', ''))
        await chairman_queries.set_active_comp_for_chairman(call.from_user.id, compId)
        await call.message.answer('Действие обработано')
