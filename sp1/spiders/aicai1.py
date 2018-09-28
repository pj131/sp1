# -*- coding: utf-8 -*-
import scrapy


class Aicai1Spider(scrapy.Spider):
    name = 'aicai1'
    allowed_domains = ['www.aicai.com/pages/lotnew/zq/index_gdhhspf.shtml']
    start_urls = ['https://www.aicai.com/pages/lotnew/zq/index_gdhhspf.shtml']

    def parse(self, response):
        def parse_rq(res):
            sps = []
            for lst in res.css('div.betPanel'):
                sp = {
                    'Mod': lst.css("div.rqMod::text").extract_first().strip(),
                    'sp':lst.css("div.betChan span.plMod::text").extract(),
                }
                sps.append(sp)
            return sps


        for _list in response.css("tr.jq_gdhhspf_match_select_tr"):
            yield {
                'name': _list.css("td.phaoTd::attr(pname)").extract_first(),
                'league':_list.css("td.saiTd span::text").extract_first(),
                'stoptime': _list.css("td.stopTd::text").extract_first(),
                'zhuan': _list.css("td.zhuanTd div span a::text").extract_first(),
                'zhu': _list.css("td.zhuTeamTd span.dmMod::text").extract_first(),
                'ke': _list.css("td.keTeamTd span.dmMod::text").extract_first(),
                'rq': parse_rq(_list.css("td.rqTd")),
            }
        print('................')

