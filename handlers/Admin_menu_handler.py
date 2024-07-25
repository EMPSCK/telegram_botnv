from aiogram import Router, F
from aiogram import types
from keyboards import admins_kb
from queries import get_user_status_query
from queries import admins_queries
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
router = Router()

class Create_comp(StatesGroup):
    next_create_comp_state = State()

#Создать новый турнир
@router.callback_query(F.data == 'create_competition')
async def cmd_start(call: types.CallbackQuery, state:FSMContext):
    user_status = await get_user_status_query.get_user_status(call.from_user.id)
    if user_status == 1:
        text = 'В следующем сообщении отправьте значения столбцов:\n\n1)compGuid\n2)date1\n3)date2\n4)compName\n5)city\n6)chairman_Id\n7)scrutineerId\n8)lin_const\n9)isActive\n10)isSecret'
        await call.message.edit_text(text=text, reply_markup=admins_kb.create_comp_kb)
        await state.set_state(Create_comp.next_create_comp_state)


@router.message(Create_comp.next_create_comp_state)
async def f2(message: Message, state: FSMContext):
    new_comp_status = await admins_queries.create_new_comp(message.text)
    if new_comp_status == 1:
        await message.answer('Запись создана', reply_markup=admins_kb.create_comp_kb)
        await state.clear()
    else:
        await message.answer('🤔Ошибка, попробуйте еще раз', reply_markup=admins_kb.create_comp_kb)



@router.callback_query(F.data == 'cancel_create_comp')
async def f4(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text('👋Добро пожаловать в admin интерфейс бота SS6', reply_markup=admins_kb.menu_kb)


#Вывести список турниров
@router.callback_query(F.data == 'show_tournament_list')
async def cmd_start(call: types.CallbackQuery, state:FSMContext):
    user_status = await get_user_status_query.get_user_status(call.from_user.id)
    if user_status == 1:
        text = await admins_queries.get_tournament_list()
        await call.message.answer(text=text)

#Редактировать турнир
class Edit_comp(StatesGroup):
    next_edit_comp_state = State()
    next_edit_comp_state_2 = State()


@router.callback_query(F.data == 'edit_competition')
async def cmd_start(call: types.CallbackQuery, state:FSMContext):
    user_status = await get_user_status_query.get_user_status(call.from_user.id)
    if user_status == 1:
        text = 'Отправьте ид соревнования:'
        await call.message.edit_text(text=text, reply_markup=admins_kb.create_comp_kb)
        await state.set_state(Edit_comp.next_edit_comp_state)


@router.message(Edit_comp.next_edit_comp_state)
async def f2(message: Message, state: FSMContext):
    id = message.text
    comp_data = await admins_queries.get_tournament(id)
    if comp_data is None or  comp_data == 0:
        await message.answer('Запись не найдена', reply_markup=admins_kb.create_comp_kb)
    else:
        text = 'В следующем сообщении отправьте значения столбцов:\n\n1)compGuid\n2)date1\n3)date2\n4)compName\n5)city\n6)chairman_Id\n7)scrutineerId\n8)lin_const\n9)isActive\n10)isSecret'
        await message.answer(str(comp_data)+'\n\n' + text, reply_markup=admins_kb.create_comp_kb)
        await state.set_state(Edit_comp.next_edit_comp_state_2)


@router.message(Edit_comp.next_edit_comp_state_2)
async def f2(message: Message, state: FSMContext):
    text = message.text
    edit_comp_status = await admins_queries.edit_tournament(message.from_user.id, message.text)
    if edit_comp_status == 1:
        await message.answer('Запись создана', reply_markup=admins_kb.create_comp_kb)
        await state.clear()
    else:
        await message.answer('🤔Ошибка, попробуйте еще раз', reply_markup=admins_kb.create_comp_kb)


