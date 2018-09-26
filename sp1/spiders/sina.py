# -*- coding: utf-8 -*-
import scrapy


class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['www.sina.com.cn']
    start_urls = ['http://www.sina.com.cn/']

    def parse(self, response):
        for _list in response.css("ul.news_top li"):
            yield {
                'text': _list.css('a::text').extract_first(),
                'href': _list.css('a::attr(href)').extract_first()
            }
        print('................')
