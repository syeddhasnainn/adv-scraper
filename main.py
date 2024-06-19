import requests
import scraper_helper
import pandas as pd
from scrapy import Selector
import regex as re
from modules.sitemap_crawler import Crawler
import time
from collections import OrderedDict


target_keywords = pd.read_csv('keywords.csv',names=['keywords'],dtype=str)['keywords'].to_list()

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


def checkKeywords(url):
    if any(x in url for x in target_keywords):
        return True
        



a = time.perf_counter()
urls = Websitecrawler('https://mentign.com/')
urls = [x['url'] for x in urls]
urls = list(OrderedDict.fromkeys(urls))
print(len(urls))
print(urls)
urls = list(filter(checkKeywords,urls))
print(len(urls))
print(urls)
b = time.perf_counter()
print(b-a)