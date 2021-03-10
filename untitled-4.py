#coding=utf-8
import telebot
import requests
from random import shuffle
bot = telebot.TeleBot("TOKEN")
global game;
game=0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    
@bot.message_handler(commands=['motivate'])
def send_quotes(message):
    quote= requests.request(url='https://api.quotable.io/random',method='get')
    bot.reply_to(message, quote.json()['content']) 

@bot.message_handler(commands=['main'])
def echo_all(message):
    global game
    game=1
    bot.send_message(message.chat.id, 'Ok, lets start a game. Send me a list of players.')
    
@bot.message_handler(commands=['chat_id'])
def get_id(message):
    bot.send_message(message.chat.id, message.chat.id)
    print(message.chat.id)
@bot.message_handler(commands=['players'])
def echo_all(message):
    global game
    if game==1:
        global listofp 
        listofp = message.text.split()[1:]
        game=2
        bot.send_message(message.chat.id, 'Ok, type /kill, to kill ')
    else:
        bot.send_message(message.chat.id, 'Game hasnt started yet')

@bot.message_handler(commands=['kill'])
def echo_all(message):
    global game
    global listofp
    if game==2 and len(listofp)>1:
        shuffle(listofp)
        killed=listofp[0]
        listofp=listofp[1:]
        bot.send_message(message.chat.id, killed+ ' was killed')
        if len(listofp)==1:
            bot.send_message(message.chat.id, listofp[0]+' is the winner uhu!')
    else:
        bot.send_message(message.chat.id, 'Game hasnt started yet')
        
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.forward_from:
        print(message.forward_from.id)
        bot.send_message(message.chat.id, message.forward_from.id)
        
bot.polling()