import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from config import settings

settings.validate()

bot = Bot(settings.BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(m: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="📊 Открыть рейтинг", web_app=WebAppInfo(url=settings.APP_URL))
    ]])
    await m.answer("Нажми кнопку, чтобы открыть приложение:", reply_markup=kb)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())