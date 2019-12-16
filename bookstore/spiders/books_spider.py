import scrapy


class QuotesSpider(scrapy.Spider):
    name = "books"

    def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/page-1.html',
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url[-6]
        filename = 'books-%s.html' % page
        

        for b in response.css("article.product_pod"):
            bname=b.css("a::text").get()
            price=b.css("p.price_color::text").get()
         

            yield{
                  'Book_name':bname,
                  'Price':price,
            }
           
        next_page=response.css('li.next a::attr(href)').get()
        if next_page is not None :
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
        
        
        
        
     