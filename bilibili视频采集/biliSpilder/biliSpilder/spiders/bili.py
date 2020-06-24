# -*- coding: utf-8 -*-
import scrapy
import json
import sys
import you_get


class BiliSpider(scrapy.Spider):
    name = 'bili'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://api.bilibili.com/x/space/arc/search?mid=315551393&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp']

    def parse(self, response):
        json_data = json.loads(response.text)
        # 获取视频bvid
        bvids = json_data['data']['list']['vlist']
        for bvid in bvids:
            bvid = bvid.get('bvid')
            # 构建视频url列表
            video_url_list = []
            video_url = 'https://www.bilibili.com/video/' + bvid
            video_url_list.append(video_url)
            for url in video_url_list:
                BiliSpider.download(url)
                # print(url)

        # 获取剩下页数的视频信息
        nexturl_list = [f'https://api.bilibili.com/x/space/arc/search?mid=315551393&ps=30&tid=0&pn={page}&keyword=&order=pubdate&jsonp=jsonp' for page in range(2, 4)]
        for next_url in nexturl_list:
            yield scrapy.Request(next_url, callback=self.parse)

    def download(url):
        sys.argv = ['you-get', '-o', 'D:/video', url]
        you_get.main()
