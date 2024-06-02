from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

# запуск тесту з -s тому що потрібно вручну ввести captcha! (pytest -k "test_amazon_adding_to_cart" -s)


class AddingToCart(BasePage):
    URL = "https://www.amazon.com/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(AddingToCart.URL)

        input("deal with captcha and click enter in GitBash")

    def search_field_click(self):
        do_field_active = self.driver.find_element(By.ID, "twotabsearchtextbox")
        do_field_active.click()

    def inputing_the_name_of_searching_item(self, item_name):
        search_item_name = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_item_name.send_keys(item_name)

    def searching_for_item(self):
        search = self.driver.find_element(By.ID, "nav-search-submit-text")
        search.click()

    def choosing_an_item(self):
        choose_item = self.driver.find_element(By.LINK_TEXT, "Gone with the Wind")
        choose_item.click()

    def adding_item_to_basket(self):
        basket_button = self.driver.find_element(By.ID, "add-to-cart-button")
        basket_button.click()

    def checking_an_item_is_added(self, expected_message):
        message = self.driver.find_element(By.ID, "NATC_SMART_WAGON_CONF_MSG_SUCCESS")
        return message.text == expected_message
