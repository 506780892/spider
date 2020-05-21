# -*- coding: utf-8 -*-
import scrapy
import json


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    # 起始网页
    start_urls = ['https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=a483045b1a19c05dd2dc6c5d99aacbb3&desktop=true&page_number=0&limit=6&action=down&after_id=53&ad_interval=-1']

    def parse(self, response):
        json_data = json.loads(response.text)
        users = json_data.get('data')

        for user in users:
            content = user.get('target')
            # 判断是否有作者信息
            if content.get('question'):
                question = content.get('question')
                title = question.get("title")  # 标题
                # print(title)
                name = question.get('author')['name']  # 作者名称
                # print(name)
                content = content['content']  # 文章内容
                # print(content)
                item = {
                    'title': title,
                    'name': name,
                    'content': content
                }
                print(item)
                print('*' * 80)
                yield item

        # 提取下一页
        next_url = json_data['paging']['next']
        yield scrapy.Request(next_url, callback=self.parse)
