from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .operation import BaseOperation

class ActionMixin(BaseOperation):
    def send_by_button(self):
        try:
            send_button = self.browser.find_element(By.XPATH, self.configurations['send_key'])
            send_button.click()
        except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException) as exception:
            print(exception)
            return False
        
        return True
    