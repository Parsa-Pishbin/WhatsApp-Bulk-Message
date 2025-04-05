from os import getcwd

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
#   do operations

# show end message
