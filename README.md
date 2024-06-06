
# Automated Testing Framework
This project provides a comprehensive framework for automated testing using Python and the Pytest platform. It includes several types of testing:

- Database Testing: Automated tests for SQLite databases.
- API Testing: Automated tests for the GitHub API.
- UI Testing: Automated tests using Selenium WebDriver for Rozetka.com.ua and Amazon.com.

## Main idea of the project
The main goal of this project is to offer a well-structured and understandable framework that can help you get started with automated testing. Whether you are looking to create a new framework or improve an existing one, this example aims to assist you in tackling some critical issues that may arise during automated testing.

## Features
- Database Testing: Verify database operations using SQLite.
- API Testing: Test the functionality and performance of the GitHub API.
- UI Testing: Automate user interactions on Rozetka.com.ua and Amazon.com using Selenium WebDriver.
  
## Project structure
The project is organized as follows:

    Anastasiia-Buriakova-QA-Automation/
    ├── config/
    │   └── config.py
    ├── modules/
    │   ├── api/
    │   │   ├── clients/
    │   │   │   ├── __init__.py
    │   │   │   └── github.py
    │   ├── common/
    │   │   ├── test_database.py
    │   │   └── __init__.py
    │   ├── ui/
    │   │   └── page_object/ 
    │   │   │   ├── amazon_ui_testing.py 
    │   │   │   ├── rozetka_ui_testing.py  
    │   │   │   ├── base_page.py
    │   │   │   └── sing_in_page.py 
    ├── tests/
    │   ├── api/
    │   │   ├── test_api.py
    │   │   ├── test_fixtures.py 
    │   │   └── test_http.py
    │   ├── database/
    │   │   └── test_database.py
    │   ├── ui/
    │   │   ├── test_amazon_ui.py
    │   │   ├── test_ui_rozetka.py
    │   │   ├── test_ui_page_object.py
    │   │   └── test_ui.py
    ├── become_qa_auto.db
    ├── pytest.ini
    ├── conftest.py
    └── README.md

### Prerequisites
- python 3.12.1 and newlest
- pytest 8.2.0
- Selenium WebDriver
- SQLite
- Requests (for API testing)
  