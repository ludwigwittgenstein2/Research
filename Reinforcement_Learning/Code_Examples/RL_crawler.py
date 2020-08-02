#First Step is to crawl data from a Blog
import requests
from urllib import request, response, error, parse
from urllib.request import urlopen
from bs4 import BeautifulSoup

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://scrapy.org/', callback=self.index_page)

    @config(age=10 * 24 * 60 * ct60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }

url = "http://www.bu.edu/president/boston-university-facts-stats/"

html = urlopen(url)

soup = BeautifulSoup(html, "lxml")

title = soup.title

titleText = title.get_text()


section = soup.find_all('section', class_='facts-categories')
for elem in section:
    wrappers = elem.find_all('div')
    for x in wrappers:
        title = x.find('h5').get_text()
        print(title)
        detail = x.find_all('ul')
        for row in detail:
            for l in row.find_all('li'):
                text = l.find('p').get_text()
                value = l.find('span', class_ = 'value').get_text()
                #print (text + value)
            #print("----------")
