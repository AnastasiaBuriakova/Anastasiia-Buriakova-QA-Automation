from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "http://github.com/login"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # знаходимо поле, в яке будемо вводити неправильне імя користувача або поштову адресу
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Вводимо неправильне імя користувача або поштову адресу
        login_elem.send_keys(username)

        # знаходимо поле в яке будемо вводити не правильний пароль
        pass_elem = self.driver.find_element(By.ID, "password")

        # вводимо не правильний пароль
        pass_elem.send_keys(password)

        # знаходимо кнопку signin
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # емулюємо клік лівою кнопкою
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
