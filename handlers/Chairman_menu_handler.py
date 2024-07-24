from aiogram import Router, F
from aiogram import types
from keyboards import chairman_list_active_comp_kb
from keyboards import chairman_start_kb
from queries import set_active_comp_for_chairman_query
router = Router()

#Вернуться в меню
@router.callback_query(F.data.startswith('back_to_chairman_menu'))
async def cmd_start(call: types.CallbackQuery):
    text = '👋Добро пожаловать в chairman интерфейс бота SS6\n\n /judges - отправить список судий'
    await call.message.edit_text(text=text, reply_markup = chairman_start_kb.menu_kb)


#Выбрать активное соревнование
@router.callback_query(F.data.startswith('set_active_competition'))
async def cmd_start(call: types.CallbackQuery):
    markup = chairman_list_active_comp_kb.gen_list_comp(call.from_user.id)
    await call.message.edit_reply_markup(reply_markup=markup)


#Обработка после выбора активного соревнования
@router.callback_query(F.data.startswith('comp_'))
async def cmd_start(call: types.CallbackQuery):
    compId = int(call.data.replace('comp_', ''))
    await set_active_comp_for_chairman_query.set_active_comp_for_chairman(call.from_user.id, compId)
    await call.message.answer('Действие обработано')
