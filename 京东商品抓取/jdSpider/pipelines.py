# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class JdspiderPipeline:
    def process_item(self, item, spider):
        with open('user.txt', 'a', encoding='utf-8') as fp:
            if item.get('price'):
                fp.write('价格：')
                fp.write(item.get('price'))
                if item.get('title'):
                    fp.write('\t名称：')
                    fp.write(item.get('title'))
                if item.get('productId'):
                    fp.write('\t商家id：')
                    fp.write(item.get('productId'))
                    fp.write('\n')
        with open('content.txt', 'a', encoding='utf-8') as fp:
            if item.get('name'):
                fp.write('名称：')
                fp.write(item.get('name'))
                if item.get('content'):
                    fp.write('\t评论：')
                    fp.write(item.get('content'))
                if item.get('productId'):
                    fp.write('\t商家id：')
                    fp.write(item.get('productId'))
                    fp.write('\n')
    # def process_item(self, item, spider):
    #     def __init__(self):
    #         self.f = open('user.txt', 'a', encoding='utf-8')
    #         self.fp = open('content.txt', 'a', encoding='utf-8')
    #
    #     def process_item(self, item, spider):
    #
    #         if 'title' in str(item):
    #             print('用户信息')
    #             self.f.write(str(item) + '\n')
    #         elif 'content' in str(item):
    #             print('内容')
    #             self.fp.write(str(item) + '\n')
    #
    #         return item
    #
    #     def close_spider(self, spider):
    #         self.f.close()
    #         self.fp.close()

# 保存mysql数据库
class JdspiderMySQLPipeline(object):

    def __init__(self):
        self.client = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',  # 使用自己的用户名
            passwd='123456',  # 使用自己的密码
            db='JDSpider',  # 数据库名
            charset='utf8')

        self.cursor = self.client.cursor()

    def process_item(self, item, spider):

        if 'title' in str(item):
            sql = 'insert into user(title, price, productId) values (%s,%s,%s)'
            lis = (item['title'], item['price'], item['productId'])
            self.cursor.execute(sql, lis)
            self.client.commit()
        if 'content' in str(item):
            sql = """insert into content(content, productId) values (%s,%s)"""
            lis = (item['content'], item['productId'])
            self.cursor.execute(sql, lis)
            self.client.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.client.close()