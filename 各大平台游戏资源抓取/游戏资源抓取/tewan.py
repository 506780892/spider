import requests
import parsel

with open('特玩网传奇游戏.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"id"},{"详情页"},{"下载地址"}'
    f.write(biaoti)
    f.write('\n')

for pag in range(1, 63):
    url = f'http://www.te5.com/mgames/chuanqi/list_2266_{pag}.html'

    response = requests.get(url=url)
    response.encoding = "utf-8"
    selector = parsel.Selector(response.text)
    div_list = selector.xpath("//div[@class='game_box']//div[@class='item']")
    for div in div_list:
        name = div.xpath(".//div[@class='i1']/span/text()").get()
        id = div.xpath(".//div[@class='i2']//@href").re("es/(.*?).html")[0]
        href = div.xpath(".//div[@class='i2']//@href").get()
        res = requests.get(href)
        sel = parsel.Selector(res.text)
        down_url = sel.xpath("//div[@class='info']//div[@class='i3']/a/@href").get()
        print(name, id, href, down_url)
        with open('特玩网传奇游戏.csv', 'a', encoding='utf-8') as f:
            te = f'{name},{id},{href},{down_url}'
            f.write(te)
            f.write('\n')