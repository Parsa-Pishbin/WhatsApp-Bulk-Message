from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from os import path

from . import configs
from .operations import action, message, data


class WhatsAppBot(action.ActionMixin, message.MessageMixin, data.DataMixin):
    def __init__(self, BASE_DIR, extra_delay=0, headless=False):
        '''
        WhatsAppBot is a agent between us and whatsapp web
        '''
        
        config_path = path.join(BASE_DIR, 'core\core_config')
        self.configurations = configs.read(config_path)
        self.extra_delay = extra_delay

        service = Service(executable_path=self.configurations['web_driver_path'])
        options = Options()
        if headless:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')

        self.browser = Chrome(service=service, options=options)
