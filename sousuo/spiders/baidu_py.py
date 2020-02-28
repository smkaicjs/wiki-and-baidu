# -*- coding: utf-8 -*-
import scrapy
import logging
from sousuo.items import SousuoItem

key = input('请输入关键词: ')
logger = logging.getLogger(__name__)

class BaiduPySpider(scrapy.Spider):
    name = 'baidu_py'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['http://baike.baidu.com/item/' + key]
    print(start_urls)

    def parse(self, response):
        content_content = response.xpath("//div[@class='body-wrapper']")
        for a in content_content:
            item = SousuoItem()
            item['key_words'] = a.xpath(".//dd['@class=lemmaWgt-lemmaTitle-title']/h1/text()").extract_first()
            #内容数组处理
            kkk = a.xpath(".//div[@class='main-content']//div[@class='para']//text()").extract()
            kg = "".join(kkk)
            kg.replace("\n","")
            item['content'] = kg
            #目录数据处理
            ll = a.xpath(".//div[@class='lemmaWgt-lemmaCatalog']//text()").extract()
            lk = "".join(ll)
            lk.replace("\n","")
            item['Catalog'] = lk
            #版面换行符处理
            pa = a.xpath(".//div[@class='basic-info cmn-clearfix']//text()").extract()
            pe = "".join(pa)
            pe.replace("\n","")
            item['page'] = pe

            yield item


        logger.warning("完成:[%s]" % response.url)







