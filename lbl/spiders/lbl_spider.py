# -*- coding: utf-8 -*-

from scrapy.spiders import Spider, Request
from lbl.items import LblItem


class LblSpider(Spider):
    name = 'lbl'
    allowed_domains = ['lbldy.com']

    def start_requests(self):
        for i in range(14999, 99999):
            url_i = 'http://www.lbldy.com/movie/' + str(i) + '.html'
            yield Request(url=url_i, meta={'page': i},
                          callback=self.parse_douban)

    def parse_douban(self, response):
        page = response.meta['page']
        title = response.xpath('//*[@id="post-' + str(page) + '"]/h2/text()').extract()
        img = response.xpath('//*[@id="post-' + str(page) +'"]/div[3]//img/@src').extract()
        contents = response.xpath('//*[@id="post-' + str(page) + '"]/div[3]/p')

        items = []
        for p in contents:
            item = LblItem()
            p_str = p.xpath('a/@href').extract()
            p_text = p.xpath('a/text()').extract()

            if p_str:
                item['title'] = title
                item['content'] = p_str
                item['page'] = page
                item['img'] = img
                item['text'] = p_text
                yield item
