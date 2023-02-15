Simple Scrapy spider

The spider works for:
"https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99"

there are two working scrapers:
- int version "single_site_spider" - this version skip location choice on the site.

- localised version "single_site_spider_localised" - this version chose proposed by site localization ( left choice button on site ).

Spiders do folowing :

- parse of the html
- collect the data,
- output the data as json file, in folowing format:

{

"loc-language": String,      # only in localised version

"name": String,

"price": Double,

"color": String,

"size": Array,

}

HOW TO BUILD:

In a new vnv:

- pip install requirements.txt


HOW TO USE:

In  "mango_product_data" folder run:

for int version:

-  scrapy crawl single_site_product_scraper_int -o mango_data_int.json

for localised version:

- scrapy crawl single_site_product_scraper_loc -o mango_data_loc.json
