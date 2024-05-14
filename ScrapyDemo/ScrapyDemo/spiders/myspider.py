import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["www.electronet.gr"]
    start_urls = ["http://www.electronet.gr/"]

    def parse(self, response):
        product_titles = response.css('h2.product-title::text').getall()
        product_prices= response.css('div.product-discounted-price::text').getall()

        for title, price in zip(product_titles, product_prices):
                print("Title:", title.strip())
                print("Price:", price.strip())
                print()