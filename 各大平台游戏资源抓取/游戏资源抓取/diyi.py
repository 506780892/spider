import requests
import parsel
import re

# 第一手游网
with open('第一手游网角色扮演.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"标签"},{"id"},{"uid"},{"下载地址"}'
    f.write(biaoti)
    f.write('\n')

for pag in range(1, 359):
    url = f'https://www.diyiyou.com/game/0-1-0-1-{pag}.html'

    response = requests.get(url=url)
    selector = parsel.Selector(response.text)
    sel_list = selector.xpath("//div[@class='tab_box']/div/ul/li")
    for sel in sel_list:
        btn = sel.xpath("./a[@class='btn']/text()").get()
        if btn == "立即下载":
            name = sel.xpath("./h4/a/text()").get()
            down_url = sel.xpath("./a[@class='btn']/@href").get()
            id = re.findall("id=(.*?)&", down_url)[0]
            uid = re.findall("uid=(.*?)&", down_url)[0]
            tag = sel.xpath("./p/text()").get()
            print(name, tag, id, uid, down_url)
            with open('第一手游网角色扮演.csv', 'a', encoding='utf-8') as f:
                te = f'{name},{tag},{id},{uid},{down_url}'
                f.write(te)
                f.write('\n')