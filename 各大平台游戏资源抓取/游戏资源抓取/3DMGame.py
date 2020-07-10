import requests, parsel

# 3DMGameBT游戏
with open('3DMGameBT游戏.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"id"},{"html_id"},{"标签"},{"简介"},{"下载地址"}'
    f.write(biaoti)
    f.write('\n')

for pag in range(1, 101):
    url = f"https://shouyou.3dmgame.com/zt/teshu_24_{pag}/"


    response = requests.get(url=url)
    selector = parsel.Selector(response.text)
    sel_list = selector.xpath("//div[@class='special_info']//div[@class='warp_info']/div[@class='item']")
    for sel in sel_list:
        name = sel.xpath("./div[@class='tex']/a/text()").get()
        try:
            html_id = sel.xpath("./div[@class='tex']/a/@href").re("id/(.*?).html")[0]
        except:
            html_id = ""
        tag = sel.xpath("./div[@class='tex']/p/span/text()").get()
        dwon_url = sel.xpath("./div[@class='a_list']/a/@href").get()
        if dwon_url != None:
            try:
                id = sel.xpath("./div[@class='a_list']/a/@href").re("1_(\d+)")[0]
            except:
                id = ""
        memo = sel.xpath(".//div[@class='text']/text()").get()
        print(name, id, html_id, tag, memo, dwon_url)
        with open('3DMGameBT游戏.csv', 'a', encoding='utf-8') as f:
            te = f'{name},{id},{html_id},{tag},{memo},{dwon_url}'
            f.write(te)
            f.write('\n')