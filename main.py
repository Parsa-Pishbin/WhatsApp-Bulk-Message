from os import getcwd
from os.path import join as join_path

from core.core import WhatsAppBot
from tools.data import read_message_file, read_numbers_file, verify_numbers
from core import configs

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
    
general_configs = configs.read(join_path(BASE_DIR, 'general_config'))

wa_bot = WhatsAppBot(
    BASE_DIR,
    general_configs,
    )

wa_bot.login()

for number in NUMBERS:
    wa_bot.go_to_user_by_phone(number)
    wa_bot.wait_for_load()
    wa_bot.write_text_message(MESSAGE)
    wa_bot.log_manager.save(number, wa_bot.send_by_enter())
    
    # if wa_bot.send_by_enter():
    #     wa_bot.log_manager.save(number, True)
    # else:
    #     wa_bot.log_manager.save(number, False)


    
#   do operations

# show end message
