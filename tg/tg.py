from secret import token
import telebot
#from adapter import Adapter

#adapter = Adapter()

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_hi(message):
    bot.send_message(message.chat.id, '''
    Привет! Я Memes bot. 😱😝🔥
Помогу тебе найти друзей, которым нравятся такие же мемесы и приколюхи, как и тебе!. 
        ''')
    bot.send_message(message.chat.id, '''Отправь мне свой ник в *Tik Tok*, чтобы я понял, что тебе нравится.''', parse_mode="Markdown")

    bot.register_next_step_handler(message, get_nickname)

@bot.message_handler(func=lambda message: False, content_types=['text'])
def get_nickname(message):
    name = message.text

    # TODO: проверять валиден ли ник
    # TODO: открыты ли лайки
    # TODO: получать список айдишников лайкнутых видосов

    print(name)






bot.polling()

