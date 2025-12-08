import pytest
from qaseio_pytest import qase
from playwright.sync_api import sync_playwright
from page.page_login import LoginPage

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@qase.id(1)  # Qase 테스트 케이스 ID
def login_success(browser):
    login = LoginPage(browser)

    login.goto("https://asm6.estsecurity.com/auth/login")
    login.login("heesun@estsecurity.com", "estsoft1!")

    assert browser.url == "https://asm6.estsecurity.com/dashboard"
