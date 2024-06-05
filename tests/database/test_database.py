import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

    assert 1 == 1


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    assert users is not None


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, "печиво", "солодке", 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, "тестові", "дані", 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


@pytest.mark.database
def test_product_insert_with_huge_number():
    db = Database()
    quant_with_51_characters = 999999999999999999999999999999999999999999999999999
    db.insert_product(55, "цукерки", "баунті", quant_with_51_characters)
    # test if a system accept huge unreal quantity with 51 characters
    sweets_qnt = db.select_product_qnt_by_id(55)[0]

    assert sweets_qnt is not None


@pytest.mark.database
def test_update_quantity_with_negative_value():
    db = Database()
    db.update_product_qnt_by_id(55, -5)
    new_qnt = db.select_product_qnt_by_id(55)

    assert new_qnt is not None
    assert new_qnt[0][0] == -5


@pytest.mark.database
def test_update_customer_name_with_existing_id():
    db = Database()
    db.update_customer_name_by_id(2, "Erik")
    new_name = db.select_customer_name_by_id(2)

    assert new_name == "Erik"


@pytest.mark.database
def test_get_address_using_unexisting_name():
    db = Database()
    address = db.get_address_by_the_name("Petro")

    assert address is None


@pytest.mark.database
def test_insert_product_with_uppercase():
    db = Database()
    db.insert_product(10, "МОЛОКО", "домашнє", 15)
    new_product = db.select_product_name_by_id(10)

    assert new_product == "МОЛОКО"


@pytest.mark.database
def test_insert_number_using_numbers_instead_of_letters():
    db = Database()
    db.insert_product(11, "5", "чорна", 4)
    name = db.select_customer_name_by_id(11)

    assert name is None


@pytest.mark.database
def test_insert_empty_field():
    db = Database()
    db.insert_product(12, "", "рожева", 10)
    name = db.select_customer_name_by_id(11)

    assert name is None


@pytest.mark.database
def test_product_insert_with_text_instead_of_number():
    db = Database()
    db.insert_quantity_as_letters(65, "батончик", "снікерс", "десять")
    result = db.select_product_qnt_by_id(65)

    assert len(result) is not None
    assert result != "десять"
