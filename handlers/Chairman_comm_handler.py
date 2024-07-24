from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from queries import get_user_status_query
from queries import Scrutineer_for_Chairman_query
from queries import Chairman_for_Scrutineer_query
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from keyboards import chairman_load_list_judges_kb
from queries import get_compId_for_user_query
from queries import get_isActive_competition_query
from aiogram import types
import load_judges_list
router = Router()

class Load_list_judges(StatesGroup):
    next_step = State()

#Загрузка списка судий
@router.message(Command("judges"))
async def cmd_judes(message: Message, state:FSMContext):
    user_status = await get_user_status_query.get_user_status(message.from_user.id)
    if user_status == 3:
        active_compId_chairman = await get_compId_for_user_query.get_CompId(message.from_user.id)
        if active_compId_chairman != 0:
            is_active = await get_isActive_competition_query.active_or_not(active_compId_chairman)
            if is_active == 1:
                await message.answer('Отправьте список в формате: Судья№1, Судья№2, ..., Судья№n.',
                                     reply_markup=chairman_load_list_judges_kb.load_judges_kb)
                await state.set_state(Load_list_judges.next_step)
            else:
                await message.answer('❌Ошибка\nВыбранное соревнование не активно')
        else:
            await message.answer('❌Ошибка\nВыберите активное соревнование')


@router.message(Load_list_judges.next_step)
async def f2(message: Message, state: FSMContext):
    await load_judges_list.load_list(message.from_user.id, message.text)


@router.callback_query(F.data == 'cancel_load')
async def f4(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text('Загрузка отменена')


#Обмен сообщениями между chairman и scrutineer
@router.message()
async def f3(message: Message):
    user_status = await get_user_status_query.get_user_status(message.from_user.id)
    if user_status == 3:
        scrutineer_id = await Scrutineer_for_Chairman_query.get_Scrutineer(message.from_user.id)
        if scrutineer_id == 0:
            await message.answer('❌Ошибка\nВыберите активное соревнование')
        else:
            active_compId_chairman = await get_compId_for_user_query.get_CompId(message.from_user.id)
            is_active = await get_isActive_competition_query.active_or_not(active_compId_chairman)
            if is_active == 1:
                try:
                    await message.bot.forward_message(scrutineer_id, message.chat.id, message.message_id)
                except:
                    print(f'{scrutineer_id} - бот в бане')
            else:
                await message.answer('❌Ошибка\nВыбранное соревнование не активно')


    if user_status == 2:
        chairman_id = await Chairman_for_Scrutineer_query.get_Chairman(message.from_user.id)
        if chairman_id == 0:
            await message.answer('❌Ошибка\nНе установлен chairman_id')
        else:
            try:
                await message.bot.forward_message(chairman_id, message.chat.id, message.message_id)
            except:
                print(f'{chairman_id} - бот в бане')



