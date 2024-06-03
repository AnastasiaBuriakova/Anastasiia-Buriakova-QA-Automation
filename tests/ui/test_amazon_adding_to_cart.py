from modules.ui.page_objects.amazon_ui_testing import AddingToCart
import pytest


@pytest.mark.ui
def test_added_to_cart():

    adding_to_cart = AddingToCart()

    adding_to_cart.go_to()
    adding_to_cart.search_field_click()
    adding_to_cart.inputing_the_name_of_searching_item("gone with the wind book")
    adding_to_cart.searching_for_item()
    adding_to_cart.choosing_an_item()
    adding_to_cart.adding_item_to_cart()

    assert adding_to_cart.checking_an_item_is_added("Added to Cart")

    adding_to_cart.close()

@pytest.mark.ui
def test_adding_similar_item_to_cart():

    adding_to_cart = AddingToCart()

    adding_to_cart.go_to()
    adding_to_cart.search_field_click()
    adding_to_cart.inputing_the_name_of_searching_item("gone with the wind book")
    adding_to_cart.searching_for_item()
    adding_to_cart.choosing_an_item()
    adding_to_cart.adding_item_to_cart()
    adding_to_cart.go_to_cart()
    adding_to_cart.click_compare_button()

    assert adding_to_cart.similar_books_are_shown("Compare with similar items")

    adding_to_cart.close()


@pytest.mark.ui
def test_the_book_was_deleted():

    adding_to_cart = AddingToCart()

    adding_to_cart.go_to()
    adding_to_cart.search_field_click()
    adding_to_cart.inputing_the_name_of_searching_item("gone with the wind book")
    adding_to_cart.searching_for_item()
    adding_to_cart.choosing_an_item()
    adding_to_cart.adding_item_to_cart()
    adding_to_cart.go_to_cart()
    adding_to_cart.deleting_a_book()

    assert adding_to_cart.checking_the_book_was_deleted("Your Amazon Cart is empty.")

    adding_to_cart.close()





   
