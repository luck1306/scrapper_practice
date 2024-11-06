# BLUEPRINT | DONT EDIT

import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://berlinstartupjobs.com/engineering/",
    headers={
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })

skills = ["python", "typescript", "javascript", "rust"]

# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:
base_url = "https://berlinstartupjobs.com/skill-areas/"

def scrapping_and_print(content):
    b = BeautifulSoup(content, "html.parser")
    job_header_info = b.find_all("div", class_="bjs-jlid__meta")
    job_description_info = b.find_all("div", class_="bjs-jlid__description")
    for i in range(0, len(job_header_info)):
        company_name = job_header_info[i].find("a", class_="bjs-jlid__b").text
        job_title = job_header_info[i].find("h4").find("a").text
        description = job_description_info[i].text.strip()
        job_link = job_header_info[i].find("h4").find("a")["href"]
        print(f"{company_name}, {job_title}, {description}. {job_link}")
# engineering
print("[engineering start]")
scrapping_and_print(response.content)
print("[engineering end]\n")

# engineering/page/2
response = requests.get("https://berlinstartupjobs.com/engineering/page/2/", 
    headers={
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })
print("[engineering/page/2 start]")
scrapping_and_print(response.content)
print("[engineering/page/2 end]\n")

for i in skills:
    response = requests.get(base_url + i, 
    headers={
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })
    print(f"[{i} start]")
    scrapping_and_print(response.content)
    print(f"[{i} end]\n")

# /YOUR CODE