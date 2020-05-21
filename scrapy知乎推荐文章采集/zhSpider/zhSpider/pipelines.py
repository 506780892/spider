# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re

class ZhspiderPipeline:
    def process_item(self, item, spider):
        # 去掉文件明中可能导致OSError: [Errno 22] Invalid argument:报错的一些信息
        item['title'] = item['title'].strip("？")
        item['title'] = item['title'].strip("?")
        item['title'] = item['title'].replace('/','')
        item['title'] = item['title'].replace('\\', '')
        with open(r'D:/知乎/'+ item['title'] +'.txt', mode='w', encoding='utf-8') as fp:
            fp.write('作者：')
            fp.write(item['name'])
            fp.write('\t标题：')
            fp.write(item['title'])
            fp.write('\n')
            fp.write('内容：')
            te = item['content']
            te = re.findall('<.*?>', te)
            # 只提取文章文字内容，去掉图片等一些杂乱信息
            for t in te:
                if t:
                    item['content'] = item['content'].replace(t, '')
            fp.write(item['content'])
        # return item
