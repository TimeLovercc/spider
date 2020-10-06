import scrapy
import json

class Spider(scrapy.Spider):
    name = 'zhihu'
    start_urls = ['https://www.zhihu.com/search?type=content&q=%E7%94%B5%E5%AD%90%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6']
    # start_urls = ['https://www.zhihu.com/api/v4/search_v3?t=general&q=%E7%94%B5%E5%AD%90%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6&correction=1&offset=0&limit=20&lc_idx=0&show_all_topics=0']


    def parse(self, response):
        a = response.xpath("//a[@target='_blank']").extract()
        print(a)
        titles = response.xpath("//div[@itemprop='zhihu:question']/a/@href").extract()
        for title in titles:
            print(title)

