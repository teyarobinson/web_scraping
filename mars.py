from splinter import Browser
from bs4 import BeautifulSoup
#import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()


    mars_scrape_data = {
       'news_title': article_title, #title
       'news_p': article_paragraph_text, #paragraph
       'featured_image_url': Featured_image_url, #pic
       'mars_weather': mars_weather #twitter
   }

    return mars_scrape_data
