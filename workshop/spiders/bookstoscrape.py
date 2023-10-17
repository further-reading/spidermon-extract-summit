import scrapy


class BookstoscrapeSpider(scrapy.Spider):
    name = 'bookstoscrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for product in response.css(".product_pod"):
            yield {
                "title": product.css("img::attr(alt)").get(),
                "link": response.urljoin(product.css("a::attr(href)").get()),
            }
