import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import logging
import os

# 🔐 Telegram Bot API токенін қоршаған орта (environment variables) арқылы алу
API_TOKEN = os.getenv("8110633206:AAHwJgpPyK7vv8N9vU39fgCh1vU3MIOBYCE")

# ✅ Логтарды баптау
logging.basicConfig(level=logging.INFO)

# 🤖 Бот пен диспетчерді инициализациялау
bot = Bot(token=8110633206:AAHwJgpPyK7vv8N9vU39fgCh1vU3MIOBYCE)
dp = Dispatcher()

# 📚 **Тұлғалық даму мәзірі**
async def personal_dev_menu(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📖 Оқылған кітаптар", callback_data="read_books")],
            [InlineKeyboardButton(text="📚 Кеңес кітаптар", callback_data="recommend_books")],
            [InlineKeyboardButton(text="🎥 Пайдалы видеолар", callback_data="videos")],
            [InlineKeyboardButton(text="🌅 Күнделікті тәжірибелер", callback_data="practices")],
            [InlineKeyboardButton(text="🔙 Артқа", callback_data="back")]
        ]
    )
    await message.answer("📚 **Тұлғалық даму бөлімі**", reply_markup=keyboard)

# 📖 **Оқылған кітаптар тізімі**
async def show_books(callback: types.CallbackQuery):
    books = "📖 Оқылған кітаптар:\n- «Атомдық дағдылар» Джеймс Клир\n- «7 тиімді дағды» Стивен Кови"
    await callback.message.answer(books)

# 📚 **Кеңес кітаптар**
async def show_recommendations(callback: types.CallbackQuery):
    recommendations = "📚 Кеңес кітаптар:\n- «Тұлғаның құрылымы» Карл Юнг\n- «Дамудың 5 қадамы» Брайан Трейси"
    await callback.message.answer(recommendations)

# 🎥 **Пайдалы видеолар**
async def show_videos(callback: types.CallbackQuery):
    videos = "🎥 Пайдалы видеолар:\n1️⃣ https://youtube.com/personal-growth\n2️⃣ https://youtube.com/mindfulness-course"
    await callback.message.answer(videos)

# 🌅 **Күнделікті тәжірибелер**
async def show_practices(callback: types.CallbackQuery):
    practices = "🌅 Күнделікті тәжірибелер:\n✅ Күнделікті журнал жазу\n✅ Медитация 15 минут\n✅ SPLENDID әдісі бойынша жоспарлау"
    await callback.message.answer(practices)

# 🔙 **Артқа**
async def go_back(callback: types.CallbackQuery):
    await callback.message.answer("🔙 Артқа қайту үшін /start басыңыз.")

# 📌 **Бот командаларын тіркеу**
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("🚀 Даму платформасына қош келдіңіз! Мұнда сіз тұлғалық даму, пайдалы кітаптар мен тәжірибелер туралы ақпарат таба аласыз.")
    await personal_dev_menu(message)

@dp.callback_query(lambda c: c.data == "read_books")
async def handle_read_books(callback: types.CallbackQuery):
    await show_books(callback)

@dp.callback_query(lambda c: c.data == "recommend_books")
async def handle_recommend_books(callback: types.CallbackQuery):
    await show_recommendations(callback)

@dp.callback_query(lambda c: c.data == "videos")
async def handle_videos(callback: types.CallbackQuery):
    await show_videos(callback)

@dp.callback_query(lambda c: c.data == "practices")
async def handle_practices(callback: types.CallbackQuery):
    await show_practices(callback)

@dp.callback_query(lambda c: c.data == "back")
async def handle_back(callback: types.CallbackQuery):
    await go_back(callback)

# 🏁 **Ботты іске қосу**
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
