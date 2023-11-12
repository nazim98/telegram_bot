import random
import telepot
from time import sleep
from puns import programming_puns
from facts import fun_facts

#6677219154:AAHPjdDYYExATSJT-qBNTWbzXxvL_mXdrrc

nazim98_bot = telepot.Bot('6677219154:AAHPjdDYYExATSJT-qBNTWbzXxvL_mXdrrc')


def action(msg):
  chat_id = msg['chat']['id']
  command = msg['text']

  if command == 'Hello':
    nazim98_bot.sendMessage(chat_id, 'Hello World')

  elif command == "What is your name?":
    nazim98_bot.sendMessage(chat_id, 'My name is nazim')

  elif command == '/joke':
    nazim98_bot.sendMessage(chat_id, random.choice(programming_puns))

  elif command == '/facts':
    nazim98_bot.sendMessage(chat_id, random.choice(fun_facts))


nazim98_bot.message_loop({'chat': action})

while True:
  sleep(1)
