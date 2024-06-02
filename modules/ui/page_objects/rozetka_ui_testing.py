from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class FindParsel(BasePage):
    URL = "https://rozetka.com.ua/ua/tracking/"

    def __init__(self) -> None:
        super().__init__()

    def open_tracking(self):
        self.driver.get(FindParsel.URL)

    def try_entering_tracking_number(self, tracking_number):
        track_number = self.driver.find_element(By.ID, "searchText")

        track_number.send_keys(tracking_number)

        btn_elem = self.driver.find_element(
            By.CSS_SELECTOR, ".tracking .tracking__form__group .button"
        )

        btn_elem.click()

    def check_validation_message(self, expected_message):
        error_message = self.driver.find_element(
            By.CSS_SELECTOR, ".tracking .validation-message"
        )
        return error_message.text == expected_message
