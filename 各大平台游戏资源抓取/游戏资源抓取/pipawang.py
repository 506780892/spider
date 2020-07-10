import requests
import parsel

# 琵琶网
with open('琵琶网传奇.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"id"},{"详情页"},{"下载地址"}'
    f.write(biaoti)
    f.write('\n')

for pag in range(1, 54):
    url = f'http://www.pipaw.com/searchsite.html?keyword=%E9%AD%94%E5%B9%BB&list_type=1&page={pag}'

    response = requests.get(url=url)
    selector = parsel.Selector(response.text)
    dl_list = selector.xpath("//div[@class='main_left']//div[@class='main_left_div']//dl")
    for dl in dl_list:
        name = dl.xpath(".//dd/a/@title").get()
        href = dl.xpath(".//dd/a/@href").get().strip("\n").strip("")
        res = requests.get(url=href)
        sel = parsel.Selector(res.text)
        downcon = sel.xpath("//div[@class='fram1']/dl/dd[2]/a/p/text()").get()
        # print(downcon)
        if downcon != "暂无下载":
            downurl = sel.xpath("//div[@class='fram1']/dl/dd[2]/a/@href").get()
            id = sel.xpath("//div[@class='fram1']/dl/dd[2]/a/@href").re("id/(.*?)/phone")
            if id:
                id = id[0]
        else:
            downurl = ""
        if downcon == None:
            downurl = sel.xpath("//div[@class='d_box_con']/div[@class='d_box_1']/p/a/@href").get()
            id = sel.xpath("//div[@class='d_box_con']/div[@class='d_box_1']/p/a/@href").re("id/(.*?)/phone")
            if id:
                id = id[0]
        memo = dl.xpath(".//dd/p/text()").get().strip("\n").strip("")
        print(name, id, href, downurl)
        with open('琵琶网传奇.csv', 'a', encoding='utf-8') as f:
            te = f'{name},{id},{href},{downurl}'
            f.write(te)
            f.write('\n')




















# import os
# filePath = 'C:\\Users\\EDZ\\PycharmProjects\\untitled\\'
# print(os.listdir(filePath))