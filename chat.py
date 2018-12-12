#!/usr/bin/python3

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('Test')

bot.set_trainer(ListTrainer)

for _file in os.listdir('files'):
    chats = open('files/'+ _file,'r').readlines()
    bot.train(chats)


while True:
   request  = input('you: ')
   response = bot.get_response(request)

   print('Flash : ',response)
