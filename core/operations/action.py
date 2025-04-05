from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .operation import BaseOperation

class ActionMixin(BaseOperation):
    def send_by_button(self):
        try:
            send_button = self.browser.find_element(By.XPATH, self.configurations['chat_send_message_key'])
            send_button.click()
        except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException) as exception:
            print(exception)
            return False
        
        return True
    
    def send_by_enter(self):
        try:
            text_input = self.browser.find_element(By.XPATH, self.configurations['chat_message_input'])
        
            text_input.click()
            text_input.send_keys(Keys.RETURN)
            sleep(0.4)
        except (NoSuchElementException, ElementNotInteractableException) as exception:
            print(exception)
            return False

    def go_to_user_by_phone(self, phone_number):
        self.browser.get(self.configurations['user_search_url'] + phone_number)
    

    def wait_for_load(self):
        while True:
            try:
                self.browser.find_element(By.XPATH, self.configurations['is_page_load_by_element'])
                break
            except NoSuchElementException:
                print('wait for load')
                sleep(0.7)
        
        sleep(0.5)
        print('loaded')

    def login(self):
        self.browser.get(self.configurations['site_url'])
        
        page = self.browser.page_source
        while self.configurations['is_login_page_phrase'] in page:
            print('wait for loggin')
            sleep(0.7)
            page = self.browser.page_source
        
        print('logged in')
        self.wait_for_load()

