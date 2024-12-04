from typing import Iterable
import scrapy
from scrapy.http import Request
from start_scrapy.items import YTTitleItem, YTElementItem

class YtgameSpider(scrapy.Spider):
    name = "ytgame"
    allowed_domains = ["www.youtube.com"]
    start_urls = ["https://www.youtube.com/gaming"]

    def start_requests(self) -> Iterable[Request]:
        yield scrapy.Request(self.start_urls[0], meta={"playwright": True})


# ytd-horizontal-card-list-renderer.ytd-item-section-renderer <- section
# #header-container h2#header #title::text <- YTTitleItem.name
# #header-container a.ytd-rich-list-header-renderer::attr(\"href\") <- YTTitleItem.url

# #scroll-container #items h3 a::text <- YTElementItem.name
# #scroll-container #items h3 a::attr(\"href\") <_ YTElementItem.url
    def parse(self, response):
        
        for e in response.css("ytd-horizontal-card-list-renderer.ytd-item-section-renderer"):
            titleItem = YTTitleItem()
            titleItem["name"] = e.css("#header-container.ytd-horizontal-card-list-renderer h2#header #title::text").get()
            titleItem["url"] = e.css("#header-container.ytd-horizontal-card-list-renderer a.ytd-rich-list-header-renderer::attr(href)").get()
            titleItem["elements"] = []
            for es in e.css("#scroll-container #items h3"):
                elementItem = YTElementItem()
                elementItem["url"] = es.css("a::text").get()
                elementItem["name"] = es.css("a::attr('href')").get()
                titleItem["elements"].append(elementItem)
            if titleItem["elements"] == []: # When [Top live games]
                for es in e.css("ytd-game-details-renderer.style-scope"):
                    elementItem = YTElementItem()
                    elementItem["url"] = es.css("a::attr('href')").get()
                    elementItem["name"] = es.css("yt-formatted-string#title::text").get()
                    titleItem["elements"].append(elementItem)
            yield titleItem