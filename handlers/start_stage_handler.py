from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from queries import get_user_status_query
from keyboards import chairmans_kb
from keyboards import scrutineer_kb
from keyboards import admins_kb
router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    user_status = await get_user_status_query.get_user_status(message.from_user.id)
    #Админ
    if user_status == 1:
        await message.answer('👋Добро пожаловать в admin интерфейс бота SS6', reply_markup=admins_kb.menu_kb)

    #scrutinner
    if user_status == 2:
        await message.answer('👋Добро пожаловать в scrutineer интерфейс бота SS6', reply_markup=scrutineer_kb.menu_kb)

    #chairman
    if user_status == 3:
        await message.answer('👋Добро пожаловать в chairman интерфейс бота SS6\n\n /judges - отправить список судей', reply_markup = chairmans_kb.menu_kb)
