"""blabla"""
import requests

from bs4 import BeautifulSoup

url = "https://www.albamon.com/jobs/area?areas=G000"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
jobs = soup.find("ul", class_="SimpleRecruitList_simple-recruit-list__ul__5KKhf").find_all("li")
jobs_list = []
for e in jobs:
    location = e.find("span", class_="Typography_typography__53V55 Typography_typography--B2__60_O6 Typography_typography--regular__qCojp")
    title = e.find("span", class_="typography-paid")
    pay = e.find("span", class_="Typography_typography__53V55 Typography_typography--B2__60_O6 Typography_typography--regular__qCojp Typography_typography--bold__BbU7t list-item-recruit__salary")
    pay_type = e.find("span", class_="Chip_content__J_ZRW chip-content")
    url = e.find("a", class_="Button_button__S9rjD Button_text__5x_Cn Button_large___Kecx Button_primary__5usVQ list-item-recruit__link list-item-recruit__link--expand list-item-recruitgoogle-analytics")
    jobs_list.append({
        "location": location.text,
        "title": title.text,
        "pay": pay.text,
        "pay_type": pay_type.text,
        "url": url["href"]
    })
print(jobs_list)