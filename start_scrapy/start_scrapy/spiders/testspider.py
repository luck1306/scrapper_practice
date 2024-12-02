import scrapy


class TestspiderSpider(scrapy.Spider):
    name = "testspider"
    allowed_domains = ["www.zyte.com"]
    start_urls = ["https://www.zyte.com/blog/"]

    def parse(self, response):
        # //*[@id="main"]/main/section[2]/div/div[1]/div[1]/h2/a
        for i, text, in enumerate(
            # response.xpath("//div/h2/a/text()").getall()
            response.css("div h2 a::text")
            ):
            yield {
                "number": i,
                "text": text
            }
