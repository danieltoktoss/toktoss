import random
import telebot
bot = telebot.TeleBot('7722764483:AAF1AbYaen2rs7q_oJFrxlULRrtPJsddNiU')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Выбери глобальные проблемы:                                                                            1)/air_pollution - способы решения загрязнения воздуха                                                                                  2)/war - как не допустить войну между государствами,                             3)/global_warming - пути решения глобального потепления ')


@bot.message_handler(commands=['air_pollution'])
def send_air(message):
    g = random.randint(1, 3)
    with open(f'air/air{g}.png', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['war'])
def send_war(message):
    r = random.randint(1, 2)
    with open(f'war/war{r}.png', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['global_warming'])
def send_warm(message):
    h = random.randint(1, 2)
    with open(f'warm/warm{h}.png', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 
bot.polling(none_stop=True, interval=0)
