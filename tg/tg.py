from secret import token
import random
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
#from tiktok import checks

#from adapter import Adapter

#adapter = Adapter()

answers = []
count = 0
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
        bot.send_message(message.chat.id, "Пройди тест, чтобы я мог понять, что тебе нравится и подыскать друзей!")
        bot.send_message(message.chat.id, "Просто выбирай понравился тебе мем или нет.")
        bot.send_message(message.chat.id, "Начать тест?")
        bot.register_next_step_handler(message, question1)
    else:
        bot.send_message(message.chat.id, '''Я не знаю такой опции. Выберите одну из списка!''')


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

    if checks.get_liked_video_count(name):
        # ERROR: ошибка при вызове этого метода
        '''
        if checks.check_likes_privacy(name):
            bot.send_message(message.chat.id, checks.get_liked_video_count("ali.pritchard"))
        else:
            bot.send_message(message.chat.id, Поменяйте свои настройки конфиденциальности parse_mode="Markdown")
            bot.send_chat_action(message.chat.id, 'upload_photo')
            img = open('instruction.jpg', 'rb')
            bot.send_photo(message.chat.id, img, reply_to_message_id=message_id)
            img.close()'''
        pass
    else:
        bot.send_message(message.chat.id, '''Такого ника не существует. Попробуйте другой!''', parse_mode="Markdown")
        bot.register_next_step_handler(message, get_ticktok_nickname)

    print(name)



@bot.message_handler(func=lambda message: False, content_types=['text'])
def question1(message):
    markup = ReplyKeyboardMarkup()

    markup.add(KeyboardButton("Лайк"))
    markup.add(KeyboardButton("Дизлайк"))
        
    bot.send_chat_action(message.chat.id, 'upload_photo')
    r = random.randrange(1,5+1)
    img = open(f'memes/english/{r}.jpg', 'rb')
    bot.send_photo(message.chat.id, img, caption='Категория #1', reply_markup=markup)
    img.close() 

    bot.register_next_step_handler(message, question2)

@bot.message_handler(func=lambda message: False, content_types=['text'])
def question2(message):
    if (message.text == "Лайк"): 
            answers.append(1)
    elif (message.text == "Дизлайк"): 
            answers.append(0)
    else:
            bot.send_message(message.chat.id, 'aeae')
            bot.register_next_step_handler(message, question2)

    markup = ReplyKeyboardMarkup()

    markup.add(KeyboardButton("Лайк"))
    markup.add(KeyboardButton("Дизлайк"))


    bot.send_chat_action(message.chat.id, 'upload_photo')
    r = random.randrange(1,5+1)
    img = open(f'memes/english/{r}.jpg', 'rb')
    bot.send_photo(message.chat.id, img, caption='Категория #1', reply_markup=markup)
    img.close() 

    bot.register_next_step_handler(message, question3)

@bot.message_handler(func=lambda message: False, content_types=['text'])
def question3(message):
    if (message.text == "Лайк"): 
            answers.append(1)
    elif (message.text == "Дизлайк"): 
            answers.append(0)
    else:
            bot.send_message(message.chat.id, 'aeae')
            bot.register_next_step_handler(message, question3)

    markup = ReplyKeyboardMarkup()

    markup.add(KeyboardButton("Лайк"))
    markup.add(KeyboardButton("Дизлайк"))


    bot.send_chat_action(message.chat.id, 'upload_photo')
    r = random.randrange(1,5+1)
    img = open(f'memes/films/{r}.jpg', 'rb')
    bot.send_photo(message.chat.id, img, caption='Категория #2', reply_markup=markup)
    img.close() 

    bot.register_next_step_handler(message, question4)

@bot.message_handler(func=lambda message: False, content_types=['text'])
def question4(message):
    if (message.text == "Лайк"): 
            answers.append(1)
    elif (message.text == "Дизлайк"): 
            answers.append(0)
    else:
            bot.send_message(message.chat.id, 'aeae')
            bot.register_next_step_handler(message, question4)

    markup = ReplyKeyboardMarkup()

    markup.add(KeyboardButton("Лайк"))
    markup.add(KeyboardButton("Дизлайк"))


    bot.send_chat_action(message.chat.id, 'upload_photo')
    r = random.randrange(1,5+1)
    img = open(f'memes/films/{r}.jpg', 'rb')
    bot.send_photo(message.chat.id, img, caption='Категория #2', reply_markup=markup)
    img.close() 

    bot.register_next_step_handler(message, question5)

@bot.message_handler(func=lambda message: False, content_types=['text'])
def question5(message):
    if (message.text == "Лайк"): 
            answers.append(1)
    elif (message.text == "Дизлайк"): 
            answers.append(0)
    else:
            bot.send_message(message.chat.id, 'aeae')
            bot.register_next_step_handler(message, question5)

    markup = ReplyKeyboardMarkup()

    markup.add(KeyboardButton("Лайк"))
    markup.add(KeyboardButton("Дизлайк"))


    bot.send_chat_action(message.chat.id, 'upload_photo')
    r = random.randrange(1,5+1)
    img = open(f'memes/kalamburi/{r}.jpg', 'rb')
    bot.send_photo(message.chat.id, img, caption='Категория #3', reply_markup=markup)
    img.close() 

    bot.register_next_step_handler(message, question6)

@bot.message_handler(func=lambda message: False, content_types=['text'])
def question6(message):
    if (message.text == "Лайк"): 
            answers.append(1)
    elif (message.text == "Дизлайк"): 
            answers.append(0)
    else:
            bot.send_message(message.chat.id, 'aeae')
            bot.register_next_step_handler(message, question6)

    markup = ReplyKeyboardMarkup()

    markup.add(KeyboardButton("Лайк"))
    markup.add(KeyboardButton("Дизлайк"))


    bot.send_chat_action(message.chat.id, 'upload_photo')
    r = random.randrange(1,5+1)
    img = open(f'memes/kalamburi/{r}.jpg', 'rb')
    bot.send_photo(message.chat.id, img, caption='Категория #3', reply_markup=markup)
    img.close() 

    bot.register_next_step_handler(message, question7)

@bot.message_handler(func=lambda message: False, content_types=['text'])
def question7(message):
    if (message.text == "Лайк"): 
            answers.append(1)
    elif (message.text == "Дизлайк"): 
            answers.append(0)
    else:
            bot.send_message(message.chat.id, 'aeae')
            bot.register_next_step_handler(message, question7)

    markup = ReplyKeyboardMarkup()

    markup.add(KeyboardButton("Лайк"))
    markup.add(KeyboardButton("Дизлайк"))


    bot.send_chat_action(message.chat.id, 'upload_photo')
    r = random.randrange(1,5+1)
    img = open(f'memes/kategoria b/{r}.jpg', 'rb')
    bot.send_photo(message.chat.id, img, caption='Категория #4', reply_markup=markup)
    img.close() 

    bot.register_next_step_handler(message, question8)

@bot.message_handler(func=lambda message: False, content_types=['text'])
def question8(message):
    if (message.text == "Лайк"): 
            answers.append(1)
    elif (message.text == "Дизлайк"): 
            answers.append(0)
    else:
            bot.send_message(message.chat.id, 'aeae')
            bot.register_next_step_handler(message, question8)

    markup = ReplyKeyboardMarkup()

    markup.add(KeyboardButton("Лайк"))
    markup.add(KeyboardButton("Дизлайк"))


    bot.send_chat_action(message.chat.id, 'upload_photo')
    r = random.randrange(1,5+1)
    img = open(f'memes/kategoria b/{r}.jpg', 'rb')
    bot.send_photo(message.chat.id, img, caption='Категория #4', reply_markup=markup)
    img.close() 

    bot.register_next_step_handler(message, question9)

@bot.message_handler(func=lambda message: False, content_types=['text'])
def question9(message):
    if (message.text == "Лайк"): 
            answers.append(1)
    elif (message.text == "Дизлайк"): 
            answers.append(0)
    else:
            bot.send_message(message.chat.id, 'aeae')
            bot.register_next_step_handler(message, question9)

    markup = ReplyKeyboardMarkup()

    markup.add(KeyboardButton("Лайк"))
    markup.add(KeyboardButton("Дизлайк"))


    bot.send_chat_action(message.chat.id, 'upload_photo')
    r = random.randrange(1,5+1)
    img = open(f'memes/postironia/{r}.jpg', 'rb')
    bot.send_photo(message.chat.id, img, caption='Категория #5', reply_markup=markup)
    img.close() 

    bot.register_next_step_handler(message, question10)

@bot.message_handler(func=lambda message: False, content_types=['text'])
def question10(message):
    if (message.text == "Лайк"): 
            answers.append(1)
    elif (message.text == "Дизлайк"): 
            answers.append(0)
    else:
            bot.send_message(message.chat.id, 'aeae')
            bot.register_next_step_handler(message, question10)

    markup = ReplyKeyboardMarkup()

    markup.add(KeyboardButton("Лайк"))
    markup.add(KeyboardButton("Дизлайк"))


    bot.send_chat_action(message.chat.id, 'upload_photo')
    r = random.randrange(1,5+1)
    img = open(f'memes/postironia/{r}.jpg', 'rb')
    bot.send_photo(message.chat.id, img, caption='Категория #5', reply_markup=markup)
    img.close() 

    bot.register_next_step_handler(message, result)

@bot.message_handler(func=lambda message: False, content_types=['text'])
def result(message):
    if (message.text == "Лайк"): 
            answers.append(1)
            bot.register_next_step_handler(message, question1)
    elif (message.text == "Дизлайк"): 
            answers.append(0)
            bot.register_next_step_handler(message, question1)
    else:
            bot.send_message(message.chat.id, 'aeae')
            bot.register_next_step_handler(message, question1)

    bot.send_message(message.chat.id, "Твои ответы записаны! Сейчас мы подберём тебе друзей...")
    
    #friends, rate = adapter.get_found_test_friends(answers)
    friends = 'aaaaa'
    rate = '0000000'
    bot.send_message(message.chat.id, 
    f'''
    Лучшие совпадения среди остальных юзеров
    1: {friends[0]} - *{rate[0]}*
    2: {friends[1]} - *{rate[1]}*
    3: {friends[2]} - *{rate[2]}*
    4: {friends[3]} - *{rate[3]}*
    5: {friends[4]} - *{rate[4]}*
    ''',
    parse_mode="Markdown")

    print(answers)



bot.polling()

