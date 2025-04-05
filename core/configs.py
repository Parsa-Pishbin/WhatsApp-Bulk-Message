from configparser import ConfigParser


def read(path:str) -> dict : 
    '''read config file and return data in dict'''

    configs = {}
    config_parser = ConfigParser()
    config_parser.read(path)

    for section in config_parser:
        configs |= dict(config_parser[section])

    return configs
