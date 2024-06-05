import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # creating an object to control the browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # open http://github.com/login
    driver.get("http://github.com/login")

    # find a field in which we will enter an incorrect username or email address
    login_elem = driver.find_element(By.ID, "login_field")

    # Enter an incorrect username or email address
    login_elem.send_keys("anastasiiaburiakova@mistakeinemail.com")

    # find the field in which we will enter the wrong password
    pass_elem = driver.find_element(By.ID, "password")

    # enter a wrong password
    pass_elem.send_keys("wrong password")

    # find sign in button
    btn_elem = driver.find_element(By.NAME, "commit")

    # emulate a click with the left mouse button
    btn_elem.click()

    assert driver.title == "Sign in to GitHub · GitHub"

    driver.close()
