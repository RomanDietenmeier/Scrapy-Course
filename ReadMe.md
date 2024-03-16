# Learning to scrape following the tutorial from freeCodeCamp.org

## https://youtu.be/mBoX_JCKZTE?feature=shared

- python -m venv venv
- .\venv\Scripts\Activate.ps1
- pip install scrapy
- scrapy startproject bookscraper
- cd .\bookscraper\
- cd .\bookscraper\spiders\
- scrapy genspider bookspider books.toscrape.com
- pip install ipython
- add: `shell = ipython` in _scrapy.cfg_ for a better shell
- scrapy shell
- fetch('http://books.toscrape.com/')
- response.css('article.product_pod') //get all books on page
- response.css('article.product_pod').get() // get the first book on page
- books = response.css('article.product_pod')
- len(books) -> 20, as there are on the page NICE
- book = books[0]
- book.css('h3 a::text').get() -> 'A Light in the ...'
- book.css('.product_price .price_color::text').get() -> '£51.77'
- book.css('h3 a').attrib['href'] -> 'catalogue/a-light-in-the-attic_1000/index.html'
- write these commands into your spider!
- exit
- cd .. -> to bookscraper/bookscraper directory
- scrapy crawl bookspider -> {'name': 'A Light in the ...', 'price': '£51.77', 'url': 'catalogue/a-light-in-the-attic_1000/index.html'} ...
- now go through the pages of the site!
- scrapy shell
- fetch('http://books.toscrape.com/')
- response.css('li.next a::attr(href)').get() -> 'catalogue/page-2.html'
- exit
- add yield response.follow(next_page_url, callback=self.parse) in spider
- scrapy crawl bookspider -> now we scrape 50 pages
- scrapy shell
- fetch("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
- get output into files:
- csv is bugged as I have not always the same keys in my spider yields!
- scrapy crawl bookspider -o out.json
- scrapy crawl bookspider -o out.csv
