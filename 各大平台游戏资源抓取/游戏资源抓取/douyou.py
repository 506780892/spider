import requests
import parsel

# 逗游
with open('逗游仙侠.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"id"},{"标签"},{"简介"}'
    f.write(biaoti)
    f.write('\n')

for pag in range(1, 1034):
    url=f"https://www.doyo.cn/zhuanti/xianxia/{pag}/"


    response = requests.get(url=url, verify=False)
    # print(response.text)
    selector = parsel.Selector(response.text)
    listli = selector.xpath("//div[@class='topic_detail_b bg']//ul[@class='clearfix']/li/a[1]")
    for li in listli:
        id = li.xpath('./@href').re('game/(.*?).html')[0]
        if id:
            id = li.xpath('./@href').re('game/(.*?).html')[0]
        name = li.xpath('./div/p[@class="name"]/text()').get()
        tag = li.xpath('./div/p[@class="tag"]/span/em/text()').get()
        memo = li.xpath('./div/p[@class="txt"]/text()').get()
        print(name, id, tag, memo)
        with open('逗游仙侠.csv', 'a', encoding='utf-8') as f:
            te = f'{name},{id},{tag},{memo}'
            f.write(te)
            f.write('\n')