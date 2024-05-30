import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.ui 
def test_check_incorrect_username():
    #створення обєкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #відкриваємо сторінку http://github.com/login
    driver.get("http://github.com/login")

    #знаходимо поле, в яке будемо вводити неправильне імя користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    #Вводимо неправильне імя користувача або пощтову адресу
    login_elem.send_keys("anastasiiaburiakova@mistakeinemail.com")

    #знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    #вводимо не праильний пароль
    pass_elem.send_keys("wrong password")

    #знаходимо кнопку sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    #емулюємо клік лівою кнопкою мишки
    btn_elem.click()


    #перевіряємо, що назва сторінки така, як ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"

    #закриваємо браузер
    driver.close()