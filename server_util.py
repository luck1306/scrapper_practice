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
    chrome = p.chromium.launch(headless=False)
    ctx = chrome.new_context(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
    page = ctx.new_page()
    page.goto(source_url+"/w/", timeout=2000)
    page.get_by_text("나무위키 홈").click()
    page.locator("div._2zpLpeXL.AM9Kqr9N").hover()
    time.sleep(1)
    soup = BeautifulSoup(page.content(), "html.parser")
    popular_list = soup.find_all("li", {"class": "RaItH85y"})
    for e in popular_list[:-1]:
        url = e.find("a")["href"]
        title = e.find("span").text
        result.append([title, f"{source_url}{url}"])
    p.stop()
    # print(result)
    return result

"""
return [[headers], [values]]
"""
def search_dc(keyword: str) -> list:
    source_url = "https://www.dcinside.com"
    return [[], []]
# print(search_namu())