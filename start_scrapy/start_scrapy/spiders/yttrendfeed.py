from typing import Iterable
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from start_scrapy.items import YTTitleItem, YTElementItem



class YttrendfeedSpider(scrapy.Spider):
    name = "yttrendfeed"
    allowed_domains = ["www.youtube.com"]
    start_urls = ["https://www.youtube.com/feed/trending"]

    def start_requests(self) -> Iterable[Request]:
        yield scrapy.Request(self.start_urls[0], meta={"playwright": True})

    # ytd-item-section-renderer.style-scope <- section
    #grid-container > ytd-video-renderer.style-scope <- typical video box
    #items > .yt-horizontal-list-renderer <- video box 4 shorts
    # ytm-shorts-lockup-view-model > div > h3 > a <- shorts title and link
    #text > a -> video channel info
    def parse(self, response):
        null_te = YTTitleItem()
        null_te["name"] = "noname"
        null_te["elements"] = []
        for section in response.css("ytd-item-section-renderer.style-scope"):
            te = YTTitleItem()
            te["name"] = section.css("h2 span#title::text").get() or ""
            te["elements"] = []
            yield from self.extract_elements(section, te)
    def extract_elements(
        self,
        section: Selector,
        te: YTTitleItem
        ):
            if section.css("ytm-shorts-lockup-view-model-v2").get() is not None: # for shorts
                for es in section.css("#items > .yt-horizontal-list-renderer"):
                    e = YTElementItem()
                    e["name"] = es.css("ytm-shorts-lockup-view-model > div > h3 > a::attr(title)").get()
                    e["url"] = es.css("ytm-shorts-lockup-view-model > div > h3 > a::attr(href)").get()
                    te["elements"].append(e)
            else: # typical video
                for es in section.css("#grid-container > ytd-video-renderer.style-scope"):
                    e = YTElementItem()
                    e["name"] = es.css("#video-title::attr(title)").get()
                    e["url"] = es.css("#video-title::attr(href)").get()
                    e["channel"] = es.css("#text > a::text").get()
                    e["channel_link"] = es.css("#text > a::attr(href)").get()
                    te["elements"].append(e)
            yield te