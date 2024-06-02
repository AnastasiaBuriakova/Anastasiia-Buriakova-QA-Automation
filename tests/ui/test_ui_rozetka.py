from modules.ui.page_objects.rozetka_ui_testing import FindParsel
import pytest


@pytest.mark.ui
def test_incorrect_tracking_number():

    find_parsel = FindParsel()

    find_parsel.open_tracking()

    find_parsel.try_entering_tracking_number("1231231567898765")

    assert find_parsel.check_validation_message(
        "Невірний формат номеру посилки. Перевірте вказані символи, а також довжину номеру, яка має бути не більше 13 символів."
    )

    find_parsel.close()
