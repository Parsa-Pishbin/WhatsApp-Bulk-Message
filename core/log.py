from datetime import datetime

class LogManager:
    def __init__(self, bot, log_file_path):
        self.log_file_path = log_file_path
        self.log_text = '{}       {}       {}       ' + str(bot) + '\n'

    def save(self, number:str, status:bool):
        time = datetime.now().strftime('%Y-%m-%d  %H:%M')
        status = 'Sent' if status else 'X   '

        with open(self.log_file_path, 'a') as log_file:
            log_file.write(self.log_text.format(status, number, time))