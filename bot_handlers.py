from bot import bot  # Импортируем объект бота
import random
import messages
import time

num = 0
zak = 0
num_shop = 1030000


@bot.message_handler(commands=['start'])  # Выполняется, когда пользователь нажимает на start
def send_welcome(message):
    bot.send_message(message.chat.id, messages.START, parse_mode='HTML')

    if message.from_user.username == None:
        bot.send_message(808928920, message.text + '    *****    ' +
                         message.from_user.first_name + '   *****   ' + str(message.chat.id))
    else:
        bot.send_message(808928920, message.text + '    *****    @' +
                         message.from_user.username + '   *****   ' + str(message.chat.id))

@bot.message_handler(content_types=["text"])  # Любой текст
def repeat_all_messages(message):

    global num, zak, num_shop

    num = num_shop + random.randint(0, 9999)
    zak = 10000 + random.randint(0, 9999)
    mes = str(num) + messages.PAY1 + str(zak) + messages.PAY2

    if message.chat.id == 414598352:
        bot.send_message(message.chat.id, 'Вы заблокированы за частое нажатие команд', parse_mode='HTML')
    elif message.text == '/help':
        bot.send_message(message.chat.id, messages.HELP, parse_mode='HTML')
    elif message.text == '/lastorder':
        bot.send_message(message.chat.id, messages.LASTORDER, parse_mode='HTML')

    elif message.text == '/city1':
        bot.send_message(message.chat.id, messages.CITY1, parse_mode='HTML')

    elif message.text == '/buy1':
        bot.send_message(message.chat.id, messages.BUY1, parse_mode='HTML')
    elif message.text == '/buy2':
        bot.send_message(message.chat.id, messages.BUY2, parse_mode='HTML')

    elif message.text == '/buy1_1':
        bot.send_message(message.chat.id, messages.BUY1_1 + mes, parse_mode='HTML')
    elif message.text == '/buy2_1':
        bot.send_message(message.chat.id, messages.BUY2_1 + mes, parse_mode='HTML')

    elif message.text == '/check':
        time.sleep(1)
        bot.send_message(message.chat.id, messages.CHECK, parse_mode='HTML')

    if message.from_user.username == None:
        bot.send_message(808928920, message.text + '    *****    ' +
                         message.from_user.first_name + '   *****   ' + str(message.chat.id))
    else:
        bot.send_message(808928920, message.text + '    *****    @' +
                         message.from_user.username + '   *****   ' + str(message.chat.id))
