import scrapy


class YttrendfeedSpider(scrapy.Spider):
    name = "yttrendfeed"
    allowed_domains = ["www.youtube.com"]
    start_urls = ["https://www.youtube.com/feed/trending"]

    # ytd-item-section-renderer.style-scope <- section

    #grid-container > ytd-video-renderer.style-scope <- typical video box
    #items > .yt-horizontal-list-renderer <- video box 4 shorts
    #text > a -> video channel info
    def parse(self, response):
        pass