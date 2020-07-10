import requests, parsel

# 斗蟹网
with open('斗蟹网角色扮演.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"id"}{"详情页"},{"下载地址"}'
    f.write(biaoti)
    f.write('\n')

for pag in range(1, 251):
    url = f'https://www.douxie.com/shouji/juesem_0_0_time_{pag}'

    response = requests.get(url=url)
    selctor = parsel.Selector(response.text)
    sel_list = selctor.xpath("//div[@class='dxPxBox']//ul[@class='dxPxList dxHzwHover touming']/li")
    for sel in sel_list:
        name = sel.xpath("./div/div[@class='dxWmImg']/a/@title").get()
        href = sel.xpath("./div/div[@class='dxWmImg']/a/@href").get()
        id = sel.xpath("./div/div[@class='dxWmImg']/a/@href").re("\d+")[0]
        res = requests.get(url=href)
        se = parsel.Selector(res.text).xpath("//div[@class='dxXiMiddle']/div[1]/a/@title").get()
        if se != "下载地址":
            down_url = ""
        else:
            down_url = parsel.Selector(res.text).xpath("//div[@class='dxBdxzBox']/a/@href").get()
        print(name, id, href, down_url)
        with open('斗蟹网角色扮演.csv', 'a', encoding='utf-8') as f:
            te = f'{name},{id},{href},{down_url}'
            f.write(te)
            f.write('\n')
