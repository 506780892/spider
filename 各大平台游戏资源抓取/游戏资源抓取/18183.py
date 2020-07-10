import requests, parsel, re

with open('18183角色扮演.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"id"},{"标签"},{"类型"},{"下载地址"},{"简介"}'
    f.write(biaoti)
    f.write('\n')

for pag in range(1, 51):
    url = f"http://ku.18183.com/list-3-1-0-2-0-{pag}.html"

    response = requests.get(url=url)
    selector = parsel.Selector(response.text)
    sel_list = selector.xpath("//div[@class='pd10 rBg mt25']/ul[@class='m-games-list clearfix']/li")
    for sel in sel_list:
        href = sel.xpath("./a/@href").get()
        res = requests.get(url=href)
        res.encoding = "urf-8"
        sel = parsel.Selector(res.text)
        name = sel.xpath("//div[@class='m-games']/dl[@class='w-gamesInfo clearfix']/dd/div/h1/text()").get()
        tag = sel.xpath("//div[@class='m-games']/dl[@class='w-gamesInfo clearfix']/dd/ul/li[1]/a/text()").get()
        feature = str(sel.xpath("//div[@class='m-games']/dl[@class='w-gamesInfo clearfix']/dd/ul[@class='bin']/li[2]/a/text()").getall()).replace(",", ".").replace("[","").replace("]","").replace("'","")
        down_url = sel.xpath("//div[@class='m-games']/dl[@class='w-gamesInfo clearfix']/dd/ul[@class='btnWrap']/li[@class='andBtn']/a/@href").get()
        if down_url != None:
            # try:
            id = re.findall("3-(\d+)", down_url)
            if id:
                id = id[0]
            else:
                id = ""
            try:
                memo = sel.xpath(
                    "//div[@class='rBg pd10 ovh']//div[@class='col-gd-ny-9']/div[@class='m-games-introduce']/div/div/p/text()").get().strip().replace("\n","")
            except:
                pass
            print(name, id, tag, feature, down_url, memo)
            with open('18183角色扮演.csv', 'a', encoding='utf-8') as f:
                te = f'{name},{id},{tag},{feature},{down_url},{memo}'
                f.write(te)
                f.write('\n')