import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message, CallbackQuery
from example import yangilik
from mybuttons import menu,keyingi
import pandas as pd

TOKEN = "7150592932:AAE8t7E_wTcfbZQJtxujCT2fyVdDZPf_0vc"
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    full_name = message.from_user.full_name
    text = f"Assalomu alaykum, {full_name}. Siz bu botning /news komandasi orqali yangiliklarni kuzatib borishingiz mumkin!"
    await message.answer(text=text, reply_markup=menu)
    man = pd.DataFrame({"ID": [message.from_user.id],
                        "Username": [message.from_user.username]})
    
    man.to_csv("my_programs/telebot/users.csv", mode="a", index=False, header=False)

@dp.message(F.text == "/news")
async def send_news(message:Message) -> None:
    try:
        await message.answer(text=yangilik(), reply_markup=keyingi)
        message.delete()
    
    except:
        await message.answer(text=yangilik(), reply_markup=keyingi)
        message.delete()        
@dp.callback_query(F.data == "keyingisi")
async def keyin(callback: CallbackQuery):
    try:
        await callback.message.answer(text=yangilik(), reply_markup=keyingi)
        await callback.message.delete()
    
    except:
        await callback.message.answer(text=yangilik(), reply_markup=keyingi)
        await callback.message.delete()
@dp.message(F.text == "Admin bilan bog'lanish")
async def with_admin(message: Message):
    await message.answer_contact(first_name="Diyorbek", phone_number="+998995702083")
    await message.answer(text="Shu bizning adminimiz!")
    
async def main() -> None:

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
