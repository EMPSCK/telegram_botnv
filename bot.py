import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import start_stage_handler
from handlers import Chairman_menu_handler
from handlers import Chairman_comm_handler
from handlers import Scrutineer_menu_handler
from handlers import Admin_menu_handler

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(start_stage_handler.router)
    dp.include_router(Chairman_menu_handler.router)
    dp.include_router(Scrutineer_menu_handler.router)
    dp.include_router(Chairman_comm_handler.router)
    dp.include_router(Admin_menu_handler.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
