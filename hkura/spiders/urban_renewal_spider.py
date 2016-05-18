from scrapy.loader import ItemLoader
from hkura.items import UrbanRenewalItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class URASpider(CrawlSpider):
    name = 'ura'
    allowed_domains = ['www.ura.org.hk']
    start_urls = [
        'http://www.ura.org.hk/en/sitemaps.aspx'
    ]

    rules = (
        Rule(LinkExtractor(allow='\.aspx', allow_domains=allowed_domains), callback='print_url', follow=True),
    )

    def print_url(self, response):
        """
            @url http://www.ura.org.hk/en/schemes-and-policies/redevelopment/ura-implemented-projects/reimbursement.aspx
            @returns items 1 1
            @returns requests 0 0
            @scrapes title link html text last_updated file_urls
        """
        l = ItemLoader(item=UrbanRenewalItem(), response=response)
        l.add_xpath('title', '//title')
        l.add_value('link', response.url)
        l.add_xpath('text', '//div[@id="content"]')
        l.add_xpath('last_updated', '//div[@class="lastUpdated"]')
        return l.load_item()

