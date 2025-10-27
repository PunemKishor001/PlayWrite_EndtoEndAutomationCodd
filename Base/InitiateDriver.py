# File: Base/InitiateDriver.py
from playwright.sync_api import sync_playwright

class InitiateDriver:

    @staticmethod
    def TestLogin():
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],slow_mo=1000)
        context = browser.new_context(no_viewport=True,record_video_dir='./Videos')
        # browser = p.chromium.launch(headless=False, slow_mo=500)
        # context = browser.new_context()
        page = context.new_page()

        # Login flow
        page.goto("https://onboarding.qa.trukker.com/#/inquiry/add")
        # page.set_viewport_size({"width": 1920, "height": 1080})
        page.fill("//input[@id='username']", "test1@trukker.com")
        page.fill("//input[@id='password']", "trukker@123")
        page.click("//input[@id='kc-login']")
        page.wait_for_load_state("networkidle")

        print("✅ Login successful")
        return p, browser, context, page
