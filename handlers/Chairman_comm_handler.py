from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from queries import get_user_status_query
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from keyboards import chairmans_kb
from queries import chairman_queries
from queries import scrutineer_queries
from queries import general_queries
from aiogram import types
import load_judges_list
import config
import pymysql
router = Router()

class Load_list_judges(StatesGroup):
    next_step = State()

#Загрузка списка судей
@router.message(Command("judges"))
async def cmd_judes(message: Message, state:FSMContext):
    user_status = await get_user_status_query.get_user_status(message.from_user.id)
    if user_status == 3:
        active_compId_chairman = await general_queries.get_CompId(message.from_user.id)
        if active_compId_chairman != 0:
            is_active = await general_queries.active_or_not(active_compId_chairman)
            if is_active == 1:
                await message.answer('Отправьте список в формате: Судья№1, Судья№2, ..., Судья№n.',
                                     reply_markup=chairmans_kb.load_judges_kb)
                await state.set_state(Load_list_judges.next_step)
            else:
                await message.answer('❌Ошибка\nВыбранное соревнование не активно')
        else:
            await message.answer('❌Ошибка\nВыберите активное соревнование')


@router.message(Load_list_judges.next_step)
async def f2(message: Message, state: FSMContext):
    compid = await general_queries.get_CompId(message.from_user.id)
    await load_judges_list.load_list(message.from_user.id, message.text, compid)
    await message.answer('Список загружен')


@router.callback_query(F.data == 'cancel_load')
async def f4(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text('Загрузка отменена')



'''

@router.message()
async def f3(message: Message):
    user_status = await get_user_status_query.get_user_status(message.from_user.id)
    if user_status == 3:
        scrutineer_id = await chairman_queries.get_Scrutineer(message.from_user.id)
        if scrutineer_id == 0:
            await message.answer('❌Ошибка\nВыберите активное соревнование')
        else:
            active_compId_chairman = await general_queries.get_CompId(message.from_user.id)
            is_active = await general_queries.active_or_not(active_compId_chairman)
            if is_active == 1:
                try:
                    await message.bot.forward_message(scrutineer_id, message.chat.id, message.message_id)
                except:
                    print(f'{scrutineer_id} - бот в бане')
            else:
                await message.answer('❌Ошибка\nВыбранное соревнование не активно')


    if user_status == 2:
        chairman_id = await scrutineer_queries.get_Chairman(message.from_user.id)
        if chairman_id == 0:
            await message.answer('❌Ошибка\nНе установлен chairman_id')
        else:
            #Проверяем активно ли соревновнание в котором записан Scrutineer
            conn = pymysql.connect(
                host=config.host,
                port=3306,
                user=config.user,
                password=config.password,
                database=config.db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            with conn:
                cur = conn.cursor()
                cur.execute(f"SELECT isActive FROM competition WHERE scrutineerId = {message.from_user.id}")
                active_or_not = cur.fetchone()
                cur.close()
            active_or_not = active_or_not['isActive']
            if active_or_not == 1:
                try:
                    await message.bot.forward_message(chairman_id, message.chat.id, message.message_id)
                except:
                    print(f'{chairman_id} - бот в бане')
            else:
                await message.answer('❌Ошибка\nСоревнование не активно') 
                
'''