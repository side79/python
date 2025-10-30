from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio
import logging


from os import getenv
from dotenv import load_dotenv #read env file

load_dotenv()

TOKEN = getenv("BOT_TOKEN")

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    filename="14_less_tel_b/bot.log",
    filemode="a",        # "a" — добавлять в конец файла, "w" — перезаписывать
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(F.text == "/test")
async def start(message: types.Message):
    await message.answer("Привет! Я бот testa.")

@dp.message() # or @dp.message(~F.text.startswith("/"))  
async def echo_message(message: types.Message):
    return await message.answer(message.text)


# @dp.message()
# async def echo_message(message: types.Message, event_from_user, event_chat):
#     if message.text.startswith("/"):  # если команда
#         return False  # 👈 разрешаем идти дальше
#     await message.answer(message.text)

async def main() -> None:
    logging.info("Бот запускается...")
    await dp.start_polling(bot)
    logging.info("Бот завершил работу")

if __name__ == "__main__": 
    asyncio.run(main())