Simple Scrapy spider

The spider works for:
"https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99"

This spider do folowing :

- parse of the html
- collect the data,
- output the data as json file, in folowing format:

{

"loc-language": String,

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

- scrapy crawl single_site_product_scraper_loc -o mango_data_loc.json
