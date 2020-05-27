# -*- coding: utf-8 -*-
import scrapy
import json
import re


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = [f'https://search.jd.com/s_new.php?keyword=%E9%9B%B6%E9%A3%9F&qrst=1&stock=1&page={pag}&s=52&click=0' for pag in range(1, 100)]

    def parse(self, response):
        selectors = response.xpath('//div[@id="J_goodsList"]/ul/li')
        for selector in selectors:
            # 价格
            price = selector.xpath('.//div[@class="p-price"]//i/text()').get()
            # 标题
            title = selector.xpath('.//div[contains(@class,"p-name")]//em//text()').getall()
            # 商品id
            productId = selector.xpath('./@data-sku').get()
            item = {
                'price': price,
                'title': ''.join(title),
                'productId': productId
            }
            # print(item)
            comment_url = f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={productId}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1'
            # 返回item
            yield item
            # 返回商品评论url
            yield scrapy.Request(comment_url, meta={'productId': productId}, callback=self.parseComment)
    # 商品评论
    def parseComment(self, response):
        productId = response.meta.get('productId')
        # 去除干扰信息，并将字符串转换为字典格式
        responses = response.text.replace('fetchJSON_comment98(', '').replace(');', '')
        data = json.loads(responses)
        # 评论最大页数
        maxPage = data.get('maxPage')
        # print(data.get('comments'))
        if data.get('comments'):
            for dat in data['comments']:
                content = dat.get('content')
                name = dat.get('nickname')
                print(name, content)
                itmes = {
                    "name": name,  # 评论名称
                    "content": content,  # 评论内容
                    # "maxPage": maxPage,
                    'productId': productId  # 商家id
                }
                yield itmes

        # 评论翻页
        if data.get('comments'):
            print(response.url)
            for page in range(1, 100):
                # print(response.url)
                maxPageUrl = re.sub('page=\d+', f'page={page}', response.url)
                print(maxPageUrl)
                yield scrapy.Request(maxPageUrl, callback=self.parseComment, meta={'productId': productId})