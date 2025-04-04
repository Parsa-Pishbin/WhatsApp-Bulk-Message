from os.path import join
from re import fullmatch

def read_message_file(dir_path:str) -> str:
    '''read message.txt and return the content'''
    
    message_file = join(dir_path, 'message.txt')
    try:
        with open(message_file, encoding="utf8") as file:
            message = file.read()
    except FileNotFoundError as exception:
        print(exception)
        return
    
    if message:
        return message


def read_numbers_file(dir_path:str) -> list[str]:
    numbers_file = join(dir_path, 'numbers.txt')
    try:
        with open(numbers_file, encoding="utf8") as file:
            numbers = file.readlines()
    except FileNotFoundError as exception:
        print(exception)
        return

    return numbers


def verify_numbers(numbers_list:list[str]) -> list[str]:
    if numbers_list is None:
        return
    cleaned_numbers_list = map(lambda number: number.replace(' ', '').replace('\n', ''), numbers_list)
    filtered_numbers = filter(lambda number: True if fullmatch('^(\+98|0)?9\d{9}$', number) else False, cleaned_numbers_list)
    approved_numbers = list(map(lambda number: '+98' + number if number.startswith('9') else number.replace('0', '+98', 1), filtered_numbers))
    return approved_numbers
