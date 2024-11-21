import scrapy


class PagerutineSpider(scrapy.Spider):
    name = "pagerutine"
    allowed_domains = ["www.zyte.com"]
    start_urls = ["https://www.zyte.com/blog"]

    def parse(self, response):
        for url in response.css("div.post-header h2 > a::attr(\"href\")").getall():
            yield scrapy.Request(response.urljoin(url), self.parse_title_and_source)
    
    def parse_title_and_source(self, response):
        title = response.css("div.post-page-content div:nth-child(2) > h1 > span::text").get()
        if title == None:
            title = response.css("div.post-page-content div:nth-child(1) > h1 > span::text").get()
        paragraph = response.css("div.post-body > span > p::text").extract()[:5]
        
        yield {
            "title": title,
            "paragraph": "".join(paragraph)
        }