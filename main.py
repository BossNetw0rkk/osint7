######### made by Doyox777
import telebot
import config
import re
import subprocess
import time
from time import sleep


bot = telebot.TeleBot(config.TOKEN)


# /start
@bot.message_handler(commands=['start'])
def first_start(message):


    bot.send_message(message.chat.id, "Masukkan username yang akan dicari : ")

    


#/about
@bot.message_handler(commands=['about'])
def about(message):

    bot.send_message(message.chat.id, "Bot untuk mencari alamat sosial media berdasarkan username")


@bot.message_handler(content_types=["text"])
def target_func(message):
    global nickname
    global target_result
    nickname = message.text
    #   message_limit(message)
    check_splcharacter(message,nickname)
    

@bot.message_handler(content_types=["text"])
def check_splcharacter(message,user_nickname):
    specialCharacters = '[@_!#$%^&*()<>?/\|}{~:]'
    string_check = re.compile(specialCharacters)
    if((string_check.search(user_nickname) == None)) & (len(nickname) < 40):
        bot.send_message(message.chat.id, "Tunggu Sebentar . . . .")
        subprocess.call(["python ","sherlock.py " , nickname])
        target_result = open(f"{nickname}.txt")
        bot.send_message(message.chat.id, target_result.read())
    else:
        bot.send_message(message.chat.id,f"Nama tidak boleh berisi {specialCharacters} \ndan tidak melebihi 40 karakter")

#run
bot.polling(none_stop=True)
