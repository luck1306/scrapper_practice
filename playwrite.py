import time
import csv

"""playwright"""
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()

page.goto("https://www.dcinside.com/")
page.get_by_placeholder("갤러리 & 통합검색").fill("건담")
time.sleep(2)

page.keyboard.down("Enter")
time.sleep(2)
with context.expect_page() as new_page_info:
    page.locator("div.integrate_cont.gallsch_result_all").locator("li:nth-child(1)").locator("a").click()
new_page = new_page_info.value
time.sleep(2)

new_page.locator("div.array_tab.left_box").locator("button:nth-child(2)").click()
time.sleep(5)

p.stop()