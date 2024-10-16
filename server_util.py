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
    source_url = "https://search.dcinside.com"
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto(source_url)
    page.get_by_placeholder("갤러리 & 통합검색").fill(keyword)
    page.keyboard.down("Enter")
    time.sleep(1)

    with context.expect_page() as new_page_info:
        page.locator("div.integrate_cont.gallsch_result_all").locator("li:nth-child(1)").locator("a").click()
    new_page = new_page_info.value
    new_page.locator("div.array_tab.left_box").locator("button:nth-child(2)").click()
    time.sleep(1)

    soup = BeautifulSoup(new_page.content(), "html.parser")
    recommend_list = soup.find_all("tr", class_="us-post")
    result = [["제목", "작성자", "날짜", "링크"]]
    for tr in recommend_list:
        title = tr.find("a").text.replace("\n", "")
        writer = tr.find("span", class_="nickname")["title"]
        date = tr.find("td", class_="gall_date")["title"]
        link = "https://gall.dcinside.com" + tr.find("a")["href"]
        result.append([title, writer, date, link])
    p.stop()
    return result