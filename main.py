import asyncio
import os
from telebot.async_telebot import AsyncTeleBot
from telebot import types

# Инициализация бота через переменную окружения Windows
bot = AsyncTeleBot(os.environ.get('Telegram_Token'))

# Обработка команд /start и /help
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message: types.Message):
    text = 'Hi, I am New_first_testing_bot.\nJust write me something and I will repeat it!'
    await bot.reply_to(message, text)

# Эхо-ответ на любые текстовые сообщения
@bot.message_handler(func=lambda message: True)
async def echo_message(message: types.Message):
    await bot.reply_to(message, message.text)

# Правильный запуск асинхронного бота
asyncio.run(bot.infinity_polling())
