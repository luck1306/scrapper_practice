from typing import Iterable
import scrapy
from scrapy.http import Request
from start_scrapy.items import YTTitleItem

class YtgameSpider(scrapy.Spider):
    name = "ytgame"
    allowed_domains = ["www.youtube.com"]
    start_urls = ["https://www.youtube.com/gaming"]

    def start_requests(self) -> Iterable[Request]:
        yield scrapy.Request(self.start_urls[0], meta={"playwright": True})

# #header-container h2#header #title::text <- YTTitleItem.name
# #header-container a.ytd-rich-list-header-renderer::attr(\"href\") <- YTTitleItem.url

# #scroll-container #items h3 a::text <- YTElementItem.name
# #scroll-container #items h3 a::attr(\"href\") <_ YTElementItem.url
    def parse(self, response):
        for e in response.css("#header-container.ytd-horizontal-card-list-renderer"):
            titleItem = YTTitleItem()
            titleItem["name"] = e.css("h2#header #title::text").get()
            titleItem["url"] = e.css("a.ytd-rich-list-header-renderer::attr(href)").get()
            titleItem["elements"] = []

            yield titleItem