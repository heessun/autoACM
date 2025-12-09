from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = 'input[placeholder="이메일"]'
        self.password = 'input[placeholder="비밀번호"]'
        self.login_btn = "text=로그인"

    def goto(self, url, wait_until="networkidle"):
        self.page.goto(url, wait_until=wait_until)

    def login(self, user, pwd):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_btn)
