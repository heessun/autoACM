import pytest
from qase.pytest import qase
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from testpage.page_login import LoginPage

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@qase.id(1)  # Qase 테스트 케이스 ID
def test_login_success(browser):
    login = LoginPage(browser)

    login.goto("https://asm6.estsecurity.com/auth/login", wait_until="networkidle")
    login.login("heesun@estsecurity.com", "estsoft1!")

    # 로그인 후 확실히 대기
    browser.wait_for_load_state("networkidle")

    expect(browser).to_have_url("https://asm6.estsecurity.com/dashboard")
