import requests
import parsel
import re


with open('应用汇角色扮演.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"ID"},{"包名"},{"简介"},{"下载地址"}'
    f.write(biaoti)
    f.write('\n')

for pag in range(1, 204):
    url = f'http://www.appchina.com/category/417/{pag}_1_1_3_0_0_0.html'


    response = requests.get(url=url)
    selector = parsel.Selector(response.text)
    app_list = selector.xpath('//ul[@class="app-list"]//li')
    app_list1 = selector.xpath('//ul[@class="app-list"]//li//div/a[2]/text()').getall()
    for app in app_list:
        name =app.xpath("./a/img/@alt").get()
        id = app.xpath("./a/img/@src").get()
        id = re.findall("128/(.*?).png", id)[0]
        pkgid = app.xpath(".//div/a[2]/@href").get().strip("/aapp/")
        memo = app.xpath(".//div[2]/span/text()").get()
        down = app.xpath(".//div/a[2]/text()").get()
        if down == "免费下载":
            downurl = "http://www.appchina.com/" + app.xpath(".//div/a[2]/@href").get()
            res = requests.get(downurl)
            res = parsel.Selector(res.text)
            downlj = res.xpath('//div[@class="download-button direct_download"]//a/@onclick').re("this,'(.*?)'")[0]
        else:
            downlj = ""
        print(name, id, pkgid, memo, downlj)
        with open('应用汇角色扮演.csv', 'a', encoding='utf-8') as f:
            biaoti = f'{name},{id},{pkgid},{memo},{downlj}'
            f.write(biaoti)
            f.write('\n')


