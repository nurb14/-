# Telegram Bot (Python + Render)

Простой шаблон Telegram-бота на aiogram, который работает 24/7 на Render.com

## 🚀 Как развернуть:

1. Создай бота через [@BotFather](https://t.me/BotFather) и получи токен.
2. Создай репозиторий на GitHub и залей эти файлы.
3. Зарегистрируйся на [Render.com](https://render.com).
4. Создай **New → Web Service** и выбери свой репозиторий.
5. Настройки:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python bot.py`
   - Environment Variable:
     - KEY: `BOT_TOKEN`
     - VALUE: `твой_токен_из_BotFather`
6. Нажми **Deploy** 🎉
