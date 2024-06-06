from modules.ui.page_objects.sign_in_page import SignInPage
import pytest

#example from the lesson
@pytest.mark.ui
def test_check_incorrect_user_page_object():
    # creating a page object
    sign_in_page = SignInPage()

    # open http://github.com/login
    sign_in_page.go_to()

    # try to go to GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # verify that the page name is what we expect
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    sign_in_page.close()
    
