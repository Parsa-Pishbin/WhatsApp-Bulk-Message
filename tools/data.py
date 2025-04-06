from re import fullmatch

from core.exceptions import (MessageFileNotFoundError, 
                             NumbersFileNotFoundError, 
                             EmptyMessageFileError, 
                             EmptyNumbersFileError, 
                             NoApprovedNumbersError)


def read_message_file(path:str) -> str:
    '''read message.txt and return the content'''
    
    try:
        with open(path, encoding="utf8") as file:
            message = file.read()
    except FileNotFoundError as exception:
        raise MessageFileNotFoundError
    
    if message:
        return message

    raise EmptyMessageFileError
    


def read_numbers_file(path:str) -> list[str]:
    try:
        with open(path, encoding="utf8") as file:
            numbers = file.readlines()
    except FileNotFoundError as exception:
        raise NumbersFileNotFoundError

    if numbers:
        return numbers

    raise EmptyNumbersFileError


def verify_numbers(numbers_list:list[str]) -> list[str]:
    cleaned_numbers_list = map(lambda number: number.replace(' ', '').replace('\n', ''), numbers_list)
    filtered_numbers = filter(lambda number: True if fullmatch('^(\+98|0)?9\d{9}$', number) else False, cleaned_numbers_list)
    approved_numbers = list(map(lambda number: '+98' + number if number.startswith('9') else number.replace('0', '+98', 1), filtered_numbers))
    
    if approved_numbers:
        return approved_numbers

    raise NoApprovedNumbersError