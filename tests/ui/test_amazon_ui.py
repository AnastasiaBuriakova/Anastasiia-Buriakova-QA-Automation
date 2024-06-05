from modules.ui.page_objects.amazon_ui_testing import AddingToCart
import pytest


@pytest.mark.ui
def test_added_an_item_to_cart_succesfully(amazon_ui):

    amazon_ui.go_to()
    amazon_ui.search_field_click()
    amazon_ui.input_the_name_of_searching_item("gone with the wind book")
    amazon_ui.search_for_item()
    amazon_ui.choose_an_item()
    amazon_ui.add_item_to_cart()

    assert amazon_ui.check_an_item_is_added("Added to Cart")


@pytest.mark.ui
def test_similar_books_are_shown(amazon_ui):

    amazon_ui.go_to()
    amazon_ui.search_field_click()
    amazon_ui.input_the_name_of_searching_item("gone with the wind book")
    amazon_ui.search_for_item()
    amazon_ui.choose_an_item()
    amazon_ui.add_item_to_cart()
    amazon_ui.go_to_cart()
    amazon_ui.click_compare_button()

    assert amazon_ui.similar_books_are_shown("Compare with similar items")


@pytest.mark.ui
def test_the_book_was_deleted(amazon_ui):

    amazon_ui.go_to()
    amazon_ui.search_field_click()
    amazon_ui.input_the_name_of_searching_item("gone with the wind book")
    amazon_ui.search_for_item()
    amazon_ui.choose_an_item()
    amazon_ui.add_item_to_cart()
    amazon_ui.go_to_cart()
    amazon_ui.delete_a_book()

    assert amazon_ui.check_the_book_was_deleted("Your Amazon Cart is empty.")
