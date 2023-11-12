import telepot
from time import sleep

nazim98 = telepot.Bot('6677219154:AAHPjdDYYExATSJT-qBNTWbzXxvL_mXdrrc')


def action(msg):
  chat_id = msg['chat']['id']
  text = msg['text']

  if "My name is " in text:
    name = text.replace("My name is ", "")
    nazim98.sendMessage(chat_id, 'Hello' + name)


nazim98.message_loop({'chat': action})

print('running')

while True:
  sleep(1)
