from datetime import datetime

class LogManager:
    def __init__(self, bot, log_file_path, terminal_log=False):
        self.log_file_path = log_file_path
        self.log_text = '{}       {}       {}       ' + str(bot) + '\n'
        self.terminal_log = terminal_log

    def save(self, number:str, status:bool):
        time = datetime.now().strftime('%Y-%m-%d  %H:%M')
        status = 'Sent' if status else 'X   '

        log_text = self.log_text.format(status, number, time)

        with open(self.log_file_path, 'a') as log_file:
            log_file.write(log_text)
        
        if self.terminal_log:
            print(log_text)