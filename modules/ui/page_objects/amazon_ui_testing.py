from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# run the test with -s because you need to manually enter the captcha! (pytest -k "test_amazon_add_to_cart" -s)


class AddToCart(BasePage):
    URL = "https://www.amazon.com/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(AddToCart.URL)
        # run the test with -s because you need to manually enter the captcha! (pytest -k "test_amazon_add_to_cart" -s)
        input("deal with captcha and click enter in GitBash")

    def search_field_click(self):
        do_field_active = self.driver.find_element(By.ID, "twotabsearchtextbox")
        do_field_active.click()

    def input_the_name_of_searching_item(self, item_name):
        search_item_name = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_item_name.send_keys(item_name)

    def search_for_item(self):
        search = self.driver.find_element(By.ID, "nav-search-submit-text")
        search.click()

    def choose_an_item(self):
        choose_item = self.driver.find_element(By.LINK_TEXT, "Gone with the Wind")
        choose_item.click()

    def add_item_to_cart(self):
        basket_button = self.driver.find_element(By.ID, "add-to-cart-button")
        basket_button.click()

    def go_to_cart(self):
        go_cart = self.driver.find_element(By.LINK_TEXT, "Go to Cart")
        go_cart.click()

    def click_compare_button(self):
        compare_button = self.driver.find_element(
            By.CSS_SELECTOR, "#comparison-lite-modal-1451635621 input"
        )
        compare_button.click()

    def similar_books_are_shown(
        self, expected_text
    ):  # added waiting time until special part of page is downloaded
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".a-popover .a-popover-inner h1")
            )
        )
        books_shown = self.driver.find_element(
            By.CSS_SELECTOR, ".a-popover .a-popover-inner h1"
        )
        return books_shown.text == expected_text

    def delete_a_book(self):
        delete_book = self.driver.find_element(
            By.CSS_SELECTOR, ".a-declarative .a-color-link"
        )
        delete_book.click()

    def check_an_item_is_added(self, expected_message):
        message = self.driver.find_element(By.ID, "NATC_SMART_WAGON_CONF_MSG_SUCCESS")
        return message.text == expected_message

    def check_the_book_was_deleted(self, expected_text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".a-row .a-row .a-spacing-mini")
            )
        )
        book_deleted = self.driver.find_element(
            By.CSS_SELECTOR, ".a-row .a-row .a-spacing-mini"
        )
        return book_deleted.text == expected_text
