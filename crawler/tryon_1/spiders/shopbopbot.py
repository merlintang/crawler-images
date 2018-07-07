# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from tryon_1.items import TryonItem

class ShopbopbotSpider(scrapy.Spider):
    name = 'shopbopbot'
    allowed_domains = ['https://www.shopbop.com/']
    start_urls = ['https://www.shopbop.com/boutique-designer-clothing/br/v=1/13773.htm',
              'https://www.shopbop.com/our-must-haves-fashion-finds-under-200/br/v=1/28182.htm',
              'https://www.shopbop.com/our-must-haves-top-sellers/br/v=1/56675.htm?baseIndex=200',
              'https://www.shopbop.com/our-must-haves-top-sellers/br/v=1/56675.htm?baseIndex=100',
              'https://www.shopbop.com/our-must-haves-top-sellers/br/v=1/56675.htm?baseIndex=0',
              'https://www.shopbop.com/boutique-editors-picks/br/v=1/13942.htm?baseIndex=100',
              'https://www.shopbop.com/boutique-editors-picks/br/v=1/13942.htm',
              'https://www.shopbop.com/our-must-haves-fashion-finds-under-200/br/v=1/28182.htm?baseIndex=100',
              'https://www.shopbop.com/our-must-haves-fashion-finds-under-200/br/v=1/28182.htm?baseIndex=200',
              'https://www.shopbop.com/our-must-haves-fashion-finds-under-200/br/v=1/28182.htm?baseIndex=300',
             'https://www.shopbop.com/boutique-designer/br/v=1/13771.htm',
             'https://www.shopbop.com/clothing-jackets-coats-blazers/br/v=1/13418.htm',
             'https://www.shopbop.com/clothing-jackets-coats-bomber/br/v=1/13422.htm',
             'https://www.shopbop.com/clothing-dresses-casual/br/v=1/13359.htm?baseIndex=100',
             'https://www.shopbop.com/clothing-dresses-casual/br/v=1/13359.htm?baseIndex=200',
             'https://www.shopbop.com/clothing-dresses-cocktail/br/v=1/13356.htm',
             'https://www.shopbop.com/clothing-dresses-formal/br/v=1/13374.htm',
             'https://www.shopbop.com/clothes-dresses-knee-length/br/v=1/13364.htm',
             'https://www.shopbop.com/clothing-dresses-off-shoulder/br/v=1/13368.htm',
             'https://www.shopbop.com/clothing-jackets-coats-blazers/br/v=1/13418.htm',
             'https://www.shopbop.com/clothing-jackets-coats-bomber/br/v=1/13422.htm',
             'https://www.shopbop.com/clothing-jackets-coats/br/v=1/13423.htm',
             'https://www.shopbop.com/clothing-jackets-coats-denim/br/v=1/13417.htm',
             'https://www.shopbop.com/clothing-jackets-coats-leather-faux/br/v=1/13419.htm',
             'https://www.shopbop.com/clothing-jackets-coats-utility/br/v=1/13421.htm',
             'https://www.shopbop.com/clothing-jumpsuits-rompers/br/v=1/13267.htm',
             'https://www.shopbop.com/clothing-lingerie-sleepwear/br/v=1/13269.htm',
             'https://www.shopbop.com/clothing-lingerie-camisoles/br/v=1/13273.htm',
             'https://www.shopbop.com/clothing-skirts/br/v=1/13302.htm',
             'https://www.shopbop.com/clothing-skirts-knee-length/br/v=1/13304.htm',
             'https://www.shopbop.com/clothing-skirts-midi/br/v=1/13310.htm',
             'https://www.shopbop.com/skirts-maxi/br/v=1/13307.htm',
             'https://www.shopbop.com/clothing-skirts-line-full/br/v=1/13303.htm',
             'https://www.shopbop.com/skirts-pencil/br/v=1/13309.htm',
             'https://www.shopbop.com/clothing-skirts-denim/br/v=1/13305.htm',
             'https://www.shopbop.com/clothing-sweaters-knits/br/v=1/13317.htm',
             'https://www.shopbop.com/clothing-sweaters-knits-cardigans/br/v=1/13325.htm',
             'https://www.shopbop.com/clothing-jeans-exclusives/br/v=1/40789.htm',
             'https://www.shopbop.com/clothing-jeans-everyday/br/v=1/13408.htm',
             'https://www.shopbop.com/clothing-jeans-ankle/br/v=1/32663.htm',
             'https://www.shopbop.com/clothing-denim-boot-cut-jeans/br/v=1/13386.htm',
             'https://www.shopbop.com/clothes-denim-boyfriend-jeans/br/v=1/13397.htm',
             'https://www.shopbop.com/clothing-denim-cropped-jeans/br/v=1/13388.htm',
             'https://www.shopbop.com/clothes-denim-distressed-jeans/br/v=1/13396.htm',
             'https://www.shopbop.com/clothing-jeans-flare-wide-leg/br/v=1/13385.htm',
             'https://www.shopbop.com/clothes-denim-high-waisted-jeans/br/v=1/13381.htm',
             'https://www.shopbop.com/clothes-denim-overalls/br/v=1/13390.htm',
             'https://www.shopbop.com/clothing-jeans-relaxed-skinny/br/v=1/32664.htm',
             'https://www.shopbop.com/clothing-activewear-jackets/br/v=1/56908.htm',
             'https://www.shopbop.com/clothing-activewear-leggings/br/v=1/56909.htm',
             'https://www.shopbop.com/clothing-activewear-shorts-skirts/br/v=1/56910.htm',
             'https://www.shopbop.com/clothing-activewear-sports-bras/br/v=1/56911.htm',
             'https://www.shopbop.com/clothing-activewear-sweatshirts-hoodies/br/v=1/56912.htm',
             'https://www.shopbop.com/clothing-activewear-sweatpants-track-pants/br/v=1/56913.htm',
             'https://www.shopbop.com/clothing-activewear-tanks/br/v=1/56914.htm',
             'https://www.shopbop.com/clothing-activewear-tees/br/v=1/56915.htm',
             'https://www.shopbop.com/clothing-jackets-coats-utility/br/v=1/13421.htm',
             'https://www.shopbop.com/clothing-jackets-coats-trench/br/v=1/13426.htm',
             'https://www.shopbop.com/clothing-jackets-coats-leather-faux/br/v=1/13419.htm',
             'https://www.shopbop.com/clothing-jackets-coats-fur-faux/br/v=1/51897.htm',
             'https://www.shopbop.com/clothing-jackets-coats-down-puffer/br/v=1/13425.htm',
             'https://www.shopbop.com/clothing-jackets-coats-denim/br/v=1/13417.htm?baseIndex=100',
             'https://www.shopbop.com/clothing-jumpsuits-rompers/br/v=1/13267.htm?baseIndex=100',
             'https://www.shopbop.com/clothing-jumpsuits-rompers/br/v=1/13267.htm?baseIndex=200',
             'https://www.shopbop.com/clothing-jumpsuits-rompers/br/v=1/13267.htm?baseIndex=300',
             'https://www.shopbop.com/clothing-jumpsuits-rompers/br/v=1/13267.htm?baseIndex=400',
             'https://www.shopbop.com/clothing-lingerie-sleepwear-slips/br/v=1/13272.htm',
             'https://www.shopbop.com/clothing-lingerie-sleepwear/br/v=1/13270.htm',
             'https://www.shopbop.com/clothing-lingerie-sleepwear/br/v=1/13270.htm?baseIndex=100',
             'https://www.shopbop.com/clothing-lingerie-sleepwear/br/v=1/13270.htm?baseIndex=200',
             'https://www.shopbop.com/clothing-lingerie-sleepwear/br/v=1/13270.htm?baseIndex=300',
             'https://www.shopbop.com/clothing-lingerie-sleepwear-sleep-masks/br/v=1/53395.htm',
             'https://www.shopbop.com/clothing-lingerie-robes/br/v=1/13278.htm',
             'https://www.shopbop.com/clothing-maternity-tops/br/v=1/40955.htm',
             'https://www.shopbop.com/clothing-maternity-bottoms/br/v=1/40956.htm',
             'https://www.shopbop.com/clothing-maternity-dresses/br/v=1/40957.htm',
             'https://www.shopbop.com/clothing-maternity-lingerie-sleepwear/br/v=1/40958.htm',
             'https://www.shopbop.com/clothing-maternity-bags-accessories/br/v=1/40959.htm',
             'https://www.shopbop.com/clothing-pants-leggings-ankle/br/v=1/57610.htm',
             'https://www.shopbop.com/clothing-pants-leggings-boot-cut-flare/br/v=1/13292.htm',
             'https://www.shopbop.com/clothing-pants-cropped/br/v=1/13282.htm',
             'https://www.shopbop.com/clothing-pants-high-waisted/br/v=1/13294.htm',
             'https://www.shopbop.com/clothing-pants-leather/br/v=1/13290.htm',
             'https://www.shopbop.com/clothing-pants-skinny/br/v=1/13284.htm',
             'https://www.shopbop.com/clothing-pants-skinny/br/v=1/13284.htm?baseIndex=100',
             'https://www.shopbop.com/clothing-pants-leggings-sweatpants/br/v=1/13293.htm',
             'https://www.shopbop.com/clothing-pants-wide-leg/br/v=1/13283.htm',
             'https://www.shopbop.com/clothing-pants-leggings-work-ready/br/v=1/51930.htm',
             'https://www.shopbop.com/clothing-shorts-denim/br/v=1/13300.htm'
            ]

    custom_settings = {
        'FEED_URI': '../../tmp/shopclues.csv'
    }

    item_set = set()

    def parse(self, response):

        url_page = response.request.url
        category = None
        try:
            sub_pt_1 = "clothing"
            sub_pt_2 = "br"
            if url_page.find(sub_pt_1) != -1:
                start_index = url_page.index(sub_pt_1)
                url_page = url_page[start_index: url_page.index(sub_pt_2) - 1]
                category = url_page[url_page.index("-") + 1:]
            elif url_page.find("clothes") != -1:
                sub_pt_1 = "clothes"
                start_index = url_page.index(sub_pt_1)
                url_page = url_page[start_index: url_page.index(sub_pt_2) - 1]
                category = url_page[url_page.index("-") + 1:]
            else:
                sub_pt_1 = "com"
                start_index = url_page.index(sub_pt_1)
                url_page = url_page[start_index: url_page.index(sub_pt_2) - 1]
                category = url_page[url_page.index("/") + 1:]

        except Exception as inst:
            self.logger.warning('Warn to get clothe category %s with error %s', response.url, inst)

        ids = response.xpath('//li[contains(@class, "hproduct product")]/@id').extract()

        divs = response.xpath('//div[contains(@data-at, "productContainer")]')

        for div in divs:
            links = div.xpath('//a[contains(@class, "photo")]/@href').extract()
            imagelinks = div.xpath('//span[contains(@class, "productBrowseMainImage")]/img/@src').extract()

        for div in divs:
            blocks = div.xpath('//div[@class="info clearfix"]')

        for block in blocks:
            titles = block.xpath('//div[@class="title"]/text()').extract()
            brands = block.xpath('//div[@class="brand"]/text()').extract()
            prices = block.xpath('//span[@class="retail-price"]/text()').extract()

        for index in xrange(0, len(ids)):

            if ids[index] in self.item_set:
                continue
            else:
                self.item_set.add(ids[index])

            item = TryonItem()
            item['id'] = ids[index]
            item['category'] = category
            item['name'] = titles[index].strip()
            item['designer'] = brands[index].strip()
            item['price'] = prices[index]
            url = 'https://www.shopbop.com' + links[index].strip()
            item['url'] = url
            yield Request(url=url, meta={'item1': item}, callback=self.parse_covers, dont_filter=True)

    def parse_covers(self, response):

        item2 = response.meta['item1']

        # grab the URL of the cover image
        img = response.xpath('//div[contains(@id, "product-image-container")]')
        imageUrl = img.xpath('//li[@class="display-list-item active"]/img/@src').extract_first()

        imageUrl_others = img.xpath('//li[@class="display-list-item "]/img/@src').extract()

        if len(imageUrl) <= 1:
            return

        # grab the details of the image
        details = response.xpath('//div[contains(@id, "product-details-box")]')
        detail = details.xpath('//ul[@class="bulleted-attributes"]/li/text()').extract()

        if len(detail) < 1:
            return

        item = TryonItem()
        item['id'] = item2['id']
        item['category'] = item2['category']
        item['name'] = item2['name']
        item['designer'] = item2['designer']
        item['price'] = item2['price']
        item['details'] = detail
        item['imageUrl'] = imageUrl
        item['imageUrlOthers'] = imageUrl_others
        item['url'] = item2['url']

        # yield the result
        yield item