from secret import token
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from tiktok import checks

#from adapter import Adapter

#adapter = Adapter()

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_hi(message):
    bot.send_message(message.chat.id, '''
    Привет! Я Memes bot. 😱😝🔥
Помогу тебе найти друзей, которым нравятся такие же мемесы и приколюхи, как и тебе!. 
        ''')

    markup = ReplyKeyboardMarkup()

    markup.add(KeyboardButton("Умный поиск"))
    markup.add(KeyboardButton("Тест"))

    bot.send_message(message.chat.id, '''Чтобы продолжить выбери опцию из списка!''', parse_mode="Markdown", reply_markup=markup)

    bot.register_next_step_handler(message, get_option)

@bot.message_handler(func=lambda message: False, content_types=['text'])
def get_option(message):
    if (message.text == 'Умный поиск'):
        markup = ReplyKeyboardMarkup()

        markup.add(KeyboardButton("VK"))
        markup.add(KeyboardButton("TikTok"))

        bot.send_message(message.chat.id, '''Умный поиск узнает Ваши предпочтения на основе ваших групп *Vk* или лайков в *TikTok*''', \
                reply_markup=markup,\
                parse_mode="Markdown")

        bot.register_next_step_handler(message, smart_search)
    elif (message.text == 'Тест'):
        bot.send_message(message.chat.id, "")
        bot.register_next_step_handler(message, testing)
    else:
        bot.send_message(message.chat.id, '''Я не знаю такой опции. Выберите одну из списка!''')

@bot.message_handler(func=lambda message: False, content_types=['text'])
def testing:
    pass

@bot.message_handler(func=lambda message: False, content_types=['text'])
def smart_search(message):
    if (message.text == "VK"):
        # TODO: когда будет вк парсер, прикрепить его сюда
        pass
    elif (message.text == "TikTok"):
        bot.send_message(message.chat.id, '''Отправь мне свой ник в *Tik Tok*, чтобы я понял, что тебе нравится.''', parse_mode="Markdown")
        bot.register_next_step_handler(message, get_ticktok_nickname)
    else:
        bot.send_message(message.chat.id, "Выберите опцию из предложенных ниже!")
        bot.register_next_step_handler(message,smart_search)


@bot.message_handler(func=lambda message: False, content_types=['text'])
def get_ticktok_nickname(message):
    name = message.text

    if checks.is_valid_username(name):
        # ERROR: ошибка при вызове этого метода
        if checks.check_likes_privacy(name):
            bot.send_message(message.chat.id, checks.get_liked_video_count("ali.pritchard"))
        else:
            bot.send_message(message.chat.id, '''Поменяйте свои настройки конфиденциальности''', parse_mode="Markdown")
            bot.send_chat_action(message.chat.id, 'upload_photo')
            img = open('instruction.jpg', 'rb')
            bot.send_photo(message.chat.id, img, reply_to_message_id=message_id)
            img.close()
    else:
        bot.send_message(message.chat.id, '''Такого ника не существует. Попробуйте другой!''', parse_mode="Markdown")
        bot.register_next_step_handler(message, get_ticktok_nickname)

    print(name)








bot.polling()

