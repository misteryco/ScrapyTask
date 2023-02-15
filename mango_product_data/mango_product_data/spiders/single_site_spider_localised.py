import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class MidiSatinSkirtSpider(scrapy.Spider):
    name = 'localised_language_one_object_scraper'
    allowed_domains = ['shop.mango.com']
    start_urls = [
        'https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99',
    ]

    def parse(self, response):
        self.driver = webdriver.Chrome()
        wait = WebDriverWait(self.driver, 10)
        self.driver.get(response.request.url)
        time.sleep(1)
        self.driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
        time.sleep(1.5)

        language = self.driver.find_element(By.XPATH, ".//div[@class='modalForm__lang modalFormLang']/a").text
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, language))).click()
        time.sleep(10)

        name = self.driver.find_element(By.CLASS_NAME, 'product-name').text
        # print(f"{80 * '*'}")

        price = self.driver.find_element(By.CLASS_NAME, 'sr-only').get_attribute("innerHTML")
        price = float(price[16:].replace(',', '.'))
        color = self.driver.find_element(By.CLASS_NAME, 'colors-info-name').text
        sizes_selector_list = self.driver.find_elements(By.XPATH, './/div[@class="size-selector-container"]/div/ul/li')
        available_sizes = [li.find_element(By.CSS_SELECTOR, 'span').text for li in sizes_selector_list]

        yield {
            'language': language,
            'name': name,
            'price': price,
            'color': color,
            'size': available_sizes
        }
