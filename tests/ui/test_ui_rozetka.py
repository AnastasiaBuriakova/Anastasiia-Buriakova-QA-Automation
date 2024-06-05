from modules.ui.page_objects.rozetka_ui_testing import FindParsel
import pytest


@pytest.mark.ui
def test_incorrect_tracking_number(rozetka_ui):

    rozetka_ui.open_tracking()

    rozetka_ui.try_entering_tracking_number("1231231567898765")

    assert rozetka_ui.check_validation_message(
        "Невірний формат номеру посилки. Перевірте вказані символи, а також довжину номеру, яка має бути не більше 13 символів."
    )

