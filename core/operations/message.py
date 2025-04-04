from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .operation import BaseOperation

class MessageMixin(BaseOperation):
    def write_text_message(self, message:str):
        '''
        write text message in input box
        '''

        try:
            text_input = self.browser.find_element(By.XPATH, self.configurations['text_input'])
        
            text_input.click()
            text_input.clear()
            for line in message.splitlines():
                text_input.send_keys(line)
                text_input.send_keys(Keys.SHIFT ,Keys.RETURN)
        except (NoSuchElementException, ElementNotInteractableException) as exception:
            print(exception)
            return False
        
        return True
