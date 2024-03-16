import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]
    bookCount = 0

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
            relative_book_link = book.css("h3 a::attr(href)").get()
            absolute_book_link = response.urljoin(relative_book_link)

            yield scrapy.Request(absolute_book_link, callback=self.parse_book_page)

            yield {
                "url": absolute_book_link,
                "price": book.css(".product_price .price_color::text").get(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback=self.parse)

    def parse_book_page(self, response):
        book = response.css("article.product_page")
        table_rows = book.css("table tr")
        yield {
            "url": response.url,
            "name": book.css("div.product_main h1::text").get(),
            "category": response.xpath("//li[3]/a/text()").get(),
            "description": book.css("#product_description")
            .xpath(".//following-sibling::p/text()")
            .get(),
            "product type": table_rows[1].css("td::text").get(),
            "star rating": book.css(".star-rating ::attr(class)").get(),
        }
