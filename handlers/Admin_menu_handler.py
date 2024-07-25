from aiogram import Router, F
from aiogram import types
from keyboards import chairman_list_active_comp_kb
from keyboards import chairman_start_kb
from queries import set_active_comp_for_chairman_query
from queries import get_user_status_query
router = Router()


#Вернуться в меню
@router.callback_query(F.data == 'back_to_chairman_menu')
async def cmd_start(call: types.CallbackQuery):
    user_status = await get_user_status_query.get_user_status(call.from_user.id)
    if user_status == 3:
        text = '👋Добро пожаловать в chairman интерфейс бота SS6\n\n /judges - отправить список судий'
        await call.message.edit_text(text=text, reply_markup=chairman_start_kb.menu_kb)
