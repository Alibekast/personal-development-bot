import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Telegram Bot API токенін жазу
API_TOKEN = '8110633206:AAHwJgpPyK7vv8N9vU39fgCh1vU3MIOBYCE'  # Мұнда өзіңіздің API токеніңізді қойыңыз

# Логирование
logging.basicConfig(level=logging.INFO)

# Bot және Dispatcher инициализациясы
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

class PersonalDevelopmentBot:
    def __init__(self):
        self.data = {
            'personal_development': {
                'books': {
                    'read': [],
                    'recommendations': [
                        "«Атомдық дағдылар» Джеймс Клир",
                        "«7 тиімді дағды» Стивен Кови",
                        "«Тұлғаның құрылымы» Карл Юнг"
                    ]
                },
                'videos': {
                    'youtube_links': [
                        "https://youtube.com/personal-growth",
                        "https://youtube.com/mindfulness-course"
                    ]
                },
                'daily_practices': [
                    "Күнделікті журнал жазбалары",
                    "Медитация 15 минут",
                    "SPLENDID әдісі бойынша жоспарлау"
                ]
            },
            'skills_development': {
                'categories': {
                    'техникалық дағдылар': [],
                    'әлеуметтік дағдылар': [],
                    'шығармашылық дағдылар': []
                },
                'progress_tracking': {}
            },
            'time_management': {
                'schedule': {},
                'priority_matrix': []
            },
            'daily_tasks': {
                'task_list': [],
                'reminders': []
            }
        }

    # Боттың негізгі менюін көрсету
    async def show_menu(self, message: types.Message):
        await message.answer("\n🏆 Негізгі меню:\n"
                             "1. Тұлғалық даму\n"
                             "2. Дағдыларды дамыту\n"
                             "3. Уақыт басқару\n"
                             "4. Күнделікті тапсырмалар\n"
                             "5. Шығу")

    # Тұлғалық даму бөлімі
    async def personal_dev_menu(self, message: types.Message):
        await message.answer("\n📚 Тұлғалық даму бөлімі:\n"
                             "1. Оқылған кітаптар\n"
                             "2. Кеңес кітаптар\n"
                             "3. Пайдалы видеолар\n"
                             "4. Күнделікті тәжірибелер\n"
                             "5. Артқа")
    
    async def show_books(self, message: types.Message):
        books = "\n".join(self.data['personal_development']['books']['read']) or "Кітаптар жоқ."
        await message.answer(f"📖 Оқылған кітаптар тізімі:\n{books}")

    async def show_recommendations(self, message: types.Message):
        recommendations = "\n".join(self.data['personal_development']['books']['recommendations'])
        await message.answer(f"🌟 Кеңес кітаптар:\n{recommendations}")

    async def show_videos(self, message: types.Message):
        videos = "\n".join(self.data['personal_development']['videos']['youtube_links'])
        await message.answer(f"🎥 Пайдалы видеолар:\n{videos}")

    async def show_practices(self, message: types.Message):
        practices = "\n".join(self.data['personal_development']['daily_practices'])
        await message.answer(f"🌅 Күнделікті тәжірибелер:\n{practices}")

    async def handle_message(self, message: types.Message):
        if message.text == '/start':
            await message.answer("🎉 Сәлем! Менің ботыма қош келдіңіз! Өз даму жолында көмек көрсету үшін мен осындамын.")
            await self.show_menu(message)

        elif message.text == '1':
            await self.personal_dev_menu(message)

        elif message.text == '2':
            await message.answer("😎 Дағдыларды дамыту бөлімін жақында қосамыз!")
        elif message.text == '3':
            await message.answer("🗓 Уақыт басқару бөлімін жақында қосамыз!")
        elif message.text == '4':
            await message.answer("⏳ Күнделікті тапсырмалар бөлімін жақында қосамыз!")
        elif message.text == '5':
            await message.answer("🎉 Сау болыңыз!")
        else:
            await message.answer("❓ Белгісіз таңдау! Қайтадан таңдау жасаңыз.")
    
    async def process_command(self, message: types.Message):
        if message.text == '1':
            await self.show_books(message)
        elif message.text == '2':
            await self.show_recommendations(message)
        elif message.text == '3':
            await self.show_videos(message)
        elif message.text == '4':
            await self.show_practices(message)

# Ботты іске қосу
if __name__ == '__main__':
    bot_instance = PersonalDevelopmentBot()

    @dp.message_handler(commands=['start'])
    async def start_command(message: types.Message):
        await bot_instance.handle_message(message)

    @dp.message_handler()
    async def echo(message: types.Message):
        await bot_instance.handle_message(message)
    
    executor.start_polling(dp, skip_updates=True)
