import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    comic = input("검색어를 입력하세요")
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://page.kakao.com/")
    
    page.get_by_placeholder("제목, 작가를 입력하세요").click()
    for i in range(50):
        page.get_by_placeholder("제목, 작가를 입력하세요").fill(comic)
        page.get_by_placeholder("제목, 작가를 입력하세요").press("Enter")
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
print("시발들아tlqkf")
print("이런 시발 개새기들아asdasdfasdfasjhggjhgjhghjfd")
