from bs4 import BeautifulSoup
from requests import get
from playwright.sync_api import sync_playwright
import time

"""
return [rankings]
"""
def search_namu() -> list:
    source_url = "https://namu.wiki"
    result = []

    p = sync_playwright().start()
    chrome = p.chromium.launch(headless=True)
    page = chrome.new_page()
    page.goto(source_url)
    page.locator("div._2zpLpeXL.AM9Kqr9N").hover()
    time.sleep(1)
    soup = BeautifulSoup(page.content(), "html.parser")
    popular_list = soup.find_all("li", {"class": "RaItH85y"})
    for e in popular_list[:-1]:
        url = e.find("a")["href"]
        title = e.find("span").text
        result.append(f"{title} - {source_url}{url}")
    p.stop()
    return result

"""
return [[headers], [values]]
"""
def search_dc(keyword: str) -> list:
    source_url = "https://www.dcinside.com"
    return [[], []]