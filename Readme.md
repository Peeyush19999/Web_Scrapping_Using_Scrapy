# Web-Scraping-using-Scrapy


Its basically about the Scrapy framework, in which we can scrap or crawl the data from websites using recursive spiders..

In this project I take a Bookstore website named http://books.toscrape.com/ and scrap the data related to bookname and price.

--------**Install Scrapy**--------
- pip install scrapy


Make a folder as named Scrap_books

--------**In Visual Studio Code**--------
  
  Open that folder
  
  To start a project

- scarpy startproject bookstore


To creating first spider
Go to spiders folder and create a books_spider.py file

- touch books_spider.py

first spider name as "books"


To scrap books details

- scrapy crawl books

To saved parsing respone on Json file

- scrapy crawl books -o all_books.json


Thank you. 

