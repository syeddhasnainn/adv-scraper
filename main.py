import requests
import scraper_helper
import pandas as pd
from scrapy import Selector
import regex as re
from modules.sitemap_crawler import Crawler

def Websitecrawler(link):
    crawl = Crawler(domain=link,fetch=True)
    urls = crawl.run()
    return urls



def scraper():
    pass


def emailRegex(response):
    pattern = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+" \
              r"(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)" \
              r"+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    return re.findall(pattern, response)



urls = Websitecrawler('https://mentign.com/')
print(urls)