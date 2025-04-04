from os.path import join


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
