Simple Scrapy spider

The spider works for:
"https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99"

there are two working scrapers:
- first wersion "single_site_spider" dont skip location choice of the site.

- second one "single_site_spider_localised" chose proposed by site localization ( left choice button on site )

Spiders do folowing :
- parse of the html
- collect the data,
- output the data as json file, in folowing format:
{
"language": String, # only for localised version
"name": String,
"price": Double,
"color": String,
"size": Array,
}
