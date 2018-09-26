# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AicaiSpider(CrawlSpider):
    name = 'aicai'
    allowed_domains = ['https://www.aicai.com/pages/lotnew/zq/index_gdhhspf.shtml']
    start_urls = ['http://https://www.aicai.com/pages/lotnew/zq/index_gdhhspf.shtml/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
