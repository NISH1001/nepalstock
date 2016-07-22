from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from nepalstock.items import NepalstockItem

class StockSpider(BaseSpider):
    name = "stockspider"
    allowed_domains = ["nepalstock.com.np"]
    start_urls = [
            "http://www.nepalstock.com.np/main/stockwiseprices/index/1/Date/Desc/",
            #"http://www.nepalstock.com.np/stockWisePrices",
    ]

    def parse(self, response):
        next_pages = response.xpath("//div[@class='pager']/a/@href").extract()
        yield Request(response.url, callback=self.parse_stock)
        for page in next_pages[1:]:
            print(page)
            yield Request(page, callback=self.parse_stock)

    def parse_stock(self, response):
        hxs = HtmlXPathSelector(response)
        trs = response.xpath("//tr")[2:]
        for tr in trs:
            data = tr.xpath("./td/text()").extract()[1:]
            if data:
                item = NepalstockItem()
                item['date'] = data[0]
                item['total_transactions'] = data[1]
                item['total_traded_shares'] = data[2]
                item['total_traded_amount'] = data[3]
                item['max_price'] = data[4]
                item['min_price'] = data[5]
                item['close_price'] = data[6]
                yield item
