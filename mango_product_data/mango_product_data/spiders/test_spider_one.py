import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class MidiSatinSkirtSpider(scrapy.Spider):
    name = 'one_object_scraper'
    allowed_domains = ['shop.mango.com']
    start_urls = [
        'add your url here',
    ]

    def parse(self, response):
        self.driver = webdriver.Chrome()
        self.driver.get(response.request.url)
        time.sleep(1)
        self.driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
        time.sleep(1.5)
        self.driver.find_element(By.CLASS_NAME, 'icon.closeModal.icon__close.desktop.confirmacionPais').click()

        name = self.driver.find_element(By.CLASS_NAME, 'product-name').text
        # price = float(self.driver.find_element(By.CLASS_NAME, 'product-sale').text[1:])
        # price = float(self.driver.find_element(By.CLASS_NAME, 'sr-only').text)
        color = self.driver.find_element(By.CLASS_NAME, 'colors-info-name').text
        # size_selector_list = self.driver.find_elements(By.XPATH, 'PL1La X4g20')
        # size_choices = size_selector_list.find_elements(By.CSS_SELECTOR, 'span')
        # sizes = [e.get_attribute("data-size") for e in size_choices]

        yield {
            'name': name,
            # 'price': price,
            'color': color,
            # 'size': size_selector_list
        }
