from selenium.webdriver.common.by import By

import base_page

class AddonsLoginPage(base_page.BasePage):

    _page_title = 'User Login :: Add-ons for Firefox'
    _email_locator = (By.ID, 'LoginEmail')
    _password_locator = (By.ID,'LoginPassword')
    _login_button_locator = (By.CSS_SELECTOR,'#login button.prominent')  # Using css till 668749 implemented

    def login(self, email, password):
        self._type_email(email)
        self._type_password( password)
        self.selenium.find_element(*self._login_button_locator).click()

    def _type_email(self, email):
        email_field = self.selenium.find_element(*self._email_locator)
        email_field.clear()
        email_field.send_keys(email)
        
    def _type_password(self, password):
        password_field = self.selenium.find_element(*self._password_locator)
        password_field.clear()
        password_field.send_keys(password)
        