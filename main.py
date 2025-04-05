from os import getcwd

from core.core import WhatsAppBot
from tools.data import read_message_file, read_numbers_file, verify_numbers

# import read_config

BASE_DIR = getcwd()
MESSAGE = read_message_file(BASE_DIR)
NUMBERS = verify_numbers(read_numbers_file(BASE_DIR))

if not MESSAGE:
    print('message not foun')
    exit()

if not NUMBERS:
    print('numbers not foun')
    exit()
    
# read config
# send data to core

wa_bot = WhatsAppBot(BASE_DIR)

for number in NUMBERS:
    wa_bot.go_to_user_by_phone(number)
    wa_bot.wait_for_load()
    wa_bot.write_text_message(MESSAGE)
    wa_bot.send_by_enter()
    
#   do operations

# show end message
