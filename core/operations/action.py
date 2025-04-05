from time import sleep
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
    
    def send_by_enter(self):
        try:
            text_input = self.browser.find_element(By.XPATH, self.configurations['text_input'])
        
            text_input.click()
            text_input.send_keys(Keys.RETURN)
            sleep(0.4)
        except (NoSuchElementException, ElementNotInteractableException) as exception:
            print(exception)
            return False

    def go_to_user_by_phone(self, phone_number):
        self.browser.get('https://web.whatsapp.com/send?phone=' + phone_number)

    def wait_for_load(self):
        while True:
            try:
                self.browser.find_element(By.XPATH, self.configurations['load_element'])
                break
            except NoSuchElementException:
                print('wait for load')
                sleep(0.7)
        
        sleep(0.5)
        print('loaded')

    def login(self):
        self.browser.get('https://web.whatsapp.com/')
        
        page = self.browser.page_source
        while self.configurations['login_element'] in page:
            print('wait for loggin')
            sleep(0.7)
            page = self.browser.page_source
        
        print('logged in')
        self.wait_for_load()

