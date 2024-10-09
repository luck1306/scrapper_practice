"""playwright babla fasba"""
from playwright.sync_api import sync_playwright
"""time"""
import time
# import csv
from bs4 import BeautifulSoup

p = sync_playwright().start()
browser = p.chromium.launch()
context = browser.new_context()
page = context.new_page()

page.goto("https://www.dcinside.com/")
page.get_by_placeholder("갤러리 & 통합검색").fill("건담")
page.keyboard.down("Enter")

# New Page Handler <a href='https://playwright.dev/python/docs/pages#handling-new-pages'></a>
with context.expect_page() as new_page_info:
    page.locator("div.integrate_cont.gallsch_result_all").locator("li:nth-child(1)").locator("a").click()
new_page = new_page_info.value

new_page.locator("div.array_tab.left_box").locator("button:nth-child(2)").click()
time.sleep(2)

soup = BeautifulSoup(new_page.content(), "html.parser")
articles = soup.find_all("tr", {
    "data-type": "icon_recomimg",
    "class": "ub-content us-post"
    })

for e in articles:
   title: str = e.find("a").text
   name: str = e.find("td", class_="gall_writer")["data-nick"]
   date: str = e.find("td", class_="gall_date")["title"]
   url: str = f"https://gall.dcinside.com{e.find('a')['href']}"
   print(title.replace("\n", ""), end=" - ")
   print(name, end=" - ")
   print(date, end=" - ")
   print(url)

p.stop()