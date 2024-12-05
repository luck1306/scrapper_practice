import scrapy


class YttrendfeedSpider(scrapy.Spider):
    name = "yttrendfeed"
    allowed_domains = ["www.youtube.com"]
    start_urls = ["https://www.youtube.com/feed/trending"]

    #ytd-item-section-renderer.style-scope <- 메인 페이지

    # #grid-container > ytd-video-renderer.style-scope <- 실시간 음악, 게임, 영화
    def parse(self, response):
        pass
