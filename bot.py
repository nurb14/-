import os
import telebot
from telebot import types

# 🔑 Получаем токен из переменной окружения
TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)

# --- Команда /start ---
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("ℹ️ Инфо", "❓ Помощь")
    markup.row("💬 О нас", "🛠 Настройки")
    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! 😃\nЯ твой персональный бот 🤖",
        reply_markup=markup
    )

# --- Обработка обычных кнопок ---
@bot.message_handler(func=lambda message: True)
def reply_to_buttons(message):
    if message.text == "ℹ️ Инфо":
        bot.send_message(
            message.chat.id,
            "*Информация о боте*\nЯ тестовый бот на Python 🐍 с красивым меню и кнопками!",
            parse_mode="Markdown"
        )
    elif message.text == "❓ Помощь":
        bot.send_message(
            message.chat.id,
            "Просто нажимай кнопки ниже, и я дам тебе нужную информацию 🙂"
        )
    elif message.text == "💬 О нас":
        bot.send_animation(
            message.chat.id,
            "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif"
        )
        bot.send_message(message.chat.id, "Мы создаём обучающие боты для Telegram 🚀")
    elif message.text == "🛠 Настройки":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Перейти на сайт 🌐", url="https://example.com")
        btn2 = types.InlineKeyboardButton("Связаться 📩", callback_data="contact")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Настройки и контакты:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "🤔 Не понимаю. Выбери кнопку ниже!")

# --- Обработка нажатий инлайн-кнопок ---
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "contact":
        bot.send_message(call.message.chat.id, "Связаться можно через email: example@mail.com ✉️")

# --- Запуск бота ---
print("Бот с красивым меню и переменной окружения запущен...")
bot.polling()
