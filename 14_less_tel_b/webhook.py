"""
This example shows how to use webhook on behind of any reverse proxy (nginx, traefik, ingress etc.)
"""

import logging
import sys
from os import getenv
from dotenv import load_dotenv #read env file

from aiohttp import web

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.markdown import hbold
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

load_dotenv()

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")

# Webserver settings
# bind localhost only to prevent any external access
WEB_SERVER_HOST = "127.0.0.1"
# Port for incoming request from reverse proxy. Should be any available port
WEB_SERVER_PORT = 8080

# Path to webhook route, on which Telegram will send requests
WEBHOOK_PATH = f"/webhook/{TOKEN}"
# Secret key to validate requests from Telegram (optional)
WEBHOOK_SECRET = "my-secret"
# Base URL for webhook will be used to generate webhook URL for Telegram,
# in this example it is used public DNS with HTTPS support
BASE_WEBHOOK_URL = "https://smart-mugs-kick.loca.lt"

# All handlers should be attached to the Router (or Dispatcher)
router = Router()

# for command start
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

@router.message(Command("menu"))
async def show_menu(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="👋 Привет", callback_data="say_hello"),
                InlineKeyboardButton(text="❓ Кто я", callback_data="who_am_i"),
            ],
            [
                InlineKeyboardButton(text="💤 Пока", callback_data="say_bye"),
            ]
        ]
    )
    await message.answer("Выбери действие:", reply_markup=keyboard)

# --- Обработка нажатий кнопок ---
@router.callback_query(lambda c: c.data == "say_hello")
async def say_hello(callback: CallbackQuery):
    await callback.message.answer("Привет 👋")
    await callback.answer()  # обязательно подтверждаем нажатие


@router.callback_query(lambda c: c.data == "who_am_i")
async def who_am_i(callback: CallbackQuery):
    user = callback.from_user
    await callback.message.answer(f"Ты — {user.full_name} (@{user.username or 'без никнейма'})")
    await callback.answer()


@router.callback_query(lambda c: c.data == "say_bye")
async def say_bye(callback: CallbackQuery):
    await callback.message.answer("До встречи 👋")
    await callback.answer()


# for other messages
@router.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def on_startup(bot: Bot) -> None:
    # If you have a self-signed SSL certificate, then you will need to send a public
    # certificate to Telegram
    await bot.set_webhook(f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}", secret_token=WEBHOOK_SECRET, allowed_updates=["message", "callback_query"])


def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)

    # Register startup hook to initialize webhook
    dp.startup.register(on_startup)

    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Create aiohttp.web.Application instance
    app = web.Application()

    # Create an instance of request handler,
    # aiogram has few implementations for different cases of usage
    # In this example we use SimpleRequestHandler which is designed to handle simple cases
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WEBHOOK_SECRET,
    )
    # Register webhook handler on application
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dp, bot=bot)

    # And finally start webserver
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()