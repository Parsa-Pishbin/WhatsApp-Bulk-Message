class ConfigFileNotFoundError(Exception):
    def __str__(self):
        return '\n\tConfig file not found !!\n\tCheck for exist "general_config" and "core\core_config" in app root\n'
    

class EmptyMessageFileError(Exception):
    def __str__(self):
        return '\n\tThe message file is empty\n\tWrite your message in it'
    
    
class EmptyNumbersFileError(Exception):
    def __str__(self):
        return '\n\tThe numbers file is empty\n\tSet your target numbers in it'
    

class NumbersFileNotFoundError(Exception):
    def __str__(self):
        return '\n\tNumbers file not found'
    

class MessageFileNotFoundError(Exception):
    def __str__(self):
        return '\n\tMessage file not found'
    

class NoApprovedNumbersError(Exception):
    def __str__(self):
        return '\n\tThere are no any approved number in numbers file'