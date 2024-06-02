from modules.ui.page_objects.amazon_ui_testing import AddingToCart
import pytest


@pytest.mark.ui
def test_subtotal_amount():

    adding_to_cart = AddingToCart()

    adding_to_cart.go_to()
    adding_to_cart.search_field_click()
    adding_to_cart.inputing_the_name_of_searching_item("gone with the wind book")
    adding_to_cart.searching_for_item()
    adding_to_cart.choosing_an_item()
    adding_to_cart.adding_item_to_basket()

    assert adding_to_cart.checking_an_item_is_added("Added to Cart")

    adding_to_cart.close()
