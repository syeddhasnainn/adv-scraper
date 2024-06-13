import requests
import scraper_helper
import pandas as pd
from scrapy import Selector
import regex as re


def crawler():
    pass


def scraper():
    pass


def emailRegex(response):
    pattern = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+" \
              r"(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)" \
              r"+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    return re.findall(pattern, response)


