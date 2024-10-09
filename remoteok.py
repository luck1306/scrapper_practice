"""BeautifulSoup Providing Parse Html Page"""
from bs4 import BeautifulSoup
from requests import get

class CompanyInfo():
    """CompanyInfo is Company Information"""

    def __init__(self, name: str, job: str, key_words: list, url: str) -> None:
        self.name: str = name
        self.job: str = job
        self.key_words: list = key_words
        self.url: str = url    
    def __str__(self) -> str:
        return f"name: {self.name}\njob: {self.job}\nkey_words: {self.key_words}\nurl: {self.url}"
    def get_url(self) -> str:
        """get CompanyInfo's url"""
        return self.url

anything: list = ["flutter", "python", "golang"]
company_info_list: list[CompanyInfo] = []

#for e in anything:
response = get("https://remoteok.com/remote-git-jobs", timeout=1000, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
})
soup = BeautifulSoup(response.content, "html.parser")
jobs = soup.find("table", id="jobsboard").find_all("tr", "job")
for e in jobs:
    name = e.find("td", "company").find("h3").text.replace("\n", "")
    job = e.find("td", "company").find("h2").text.replace("\n", "")
    print(f"{job} -- {name}")