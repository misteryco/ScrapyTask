import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def float_conversion_with_coma_replacement(string):
    if ',' in string:
        return float(string.replace(',', '.'))

    return float(string)


class MangoSpecificProductSpiderLoc(scrapy.Spider):
    name = 'single_site_product_scraper_loc'
    allowed_domains = ['shop.mango.com']
    start_urls = [
        'https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99',
    ]

    def parse(self, response):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)

        driver.get(response.request.url)

        # accept cookies
        wait.until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))).click()
        time.sleep(5)

        # choose default localisation country
        language = driver.find_element(By.XPATH, ".//div[@class='modalForm__lang modalFormLang']/a").text
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, language))).click()
        time.sleep(5)

        # fetch product data
        name = driver.find_element(By.CLASS_NAME, 'product-name').text
        price = driver.find_element(By.CLASS_NAME, 'sr-only').get_attribute("innerHTML")[16:]
        price = float_conversion_with_coma_replacement(price)
        color = driver.find_element(By.CLASS_NAME, 'colors-info-name').text
        sizes_selector_list = driver.find_elements(By.XPATH, './/div[@class="size-selector-container"]/div/ul/li')
        available_sizes = [li.find_element(By.CSS_SELECTOR, 'span').text for li in sizes_selector_list]

        yield {
            'loc-language': language,
            'name': name,
            'price': price,
            'color': color,
            'size': available_sizes
        }
