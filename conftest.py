import pytest
from modules.api.clients.github import GitHub
from modules.ui.page_objects.rozetka_ui_testing import FindParsel
from modules.ui.page_objects.amazon_ui_testing import AddToCart


class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Anastasiia"
        self.second_name = "Buriakova"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api


@pytest.fixture
def rozetka_ui():
    find_parsel = FindParsel()

    yield find_parsel

    find_parsel.close()


@pytest.fixture
def amazon_ui():
    add_to_cart = AddToCart()

    yield add_to_cart

    add_to_cart.close()
