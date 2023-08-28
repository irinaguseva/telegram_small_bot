python
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from .config.py import BOT_TOKEN

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Определяем обработчики команд
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я чат-бот.")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Я могу отвечать на заранее предложенные вопросы.")

# Определяем обработчик сообщений
def answer(update, context):
    question = update.message.text.lower()

    # Здесь можно добавить свои вопросы и ответы
    if question == 'как дела?':
        context.bot.send_message(chat_id=update.effective_chat.id, text="У меня всё отлично!")
    elif question == 'как тебя зовут?':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Меня зовут Чатти, и я - чат-бот!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Извините, я не понимаю ваш вопрос.")

def main():
    # Создаем экземпляр класса Updater и передаем ему токен
    updater = Updater(token=BOT_TOKEN, use_context=True)

    # Получаем экземпляр диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчики команд
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)

    # Регистрируем обработчик сообщений
    answer_handler = MessageHandler(Filters.text & (~Filters.command), answer)
    dispatcher.add_handler(answer_handler)

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
