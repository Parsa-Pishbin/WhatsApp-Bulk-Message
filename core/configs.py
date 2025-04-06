from configparser import ConfigParser

from .exceptions import ConfigFileNotFoundError


def read(path:str) -> dict : 
    '''read config file and return data in dict'''

    configs = {}
    config_parser = ConfigParser()
    read_files_list = config_parser.read(path)

    if not read_files_list:
        raise ConfigFileNotFoundError
    
    for section in config_parser:
        configs |= dict(config_parser[section])

    return configs
