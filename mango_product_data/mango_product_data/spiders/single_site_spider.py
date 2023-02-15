import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class MidiSatinSkirtSpider(scrapy.Spider):
    name = 'single_site_product_scraper_int'
    allowed_domains = ['shop.mango.com']
    start_urls = [
        'https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99',
    ]

    def parse(self, response):
        driver = webdriver.Chrome()
        driver.get(response.request.url)
        time.sleep(1)
        driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
        time.sleep(1.5)
        driver.find_element(By.CLASS_NAME, 'icon.closeModal.icon__close.desktop.confirmacionPais').click()

        name = driver.find_element(By.CLASS_NAME, 'product-name').text
        price = driver.find_element(By.CLASS_NAME, 'sr-only').get_attribute("innerHTML")
        price = float(price[-5:].strip())
        color = driver.find_element(By.CLASS_NAME, 'colors-info-name').text
        sizes_selector_list = driver.find_elements(By.XPATH, './/div[@class="size-selector-container"]/div/ul/li')
        available_sizes = [li.find_element(By.CSS_SELECTOR, 'span').text for li in sizes_selector_list]

        yield {
            'name': name,
            'price': price,
            'color': color,
            'size': available_sizes
        }
