import requests
import parsel


with open('易玩角色扮演.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"id"},{"标签"},{"简介"},{"下载地址"}'
    f.write(biaoti)
    f.write('\n')
for pag in range(1, 101):
    url = f'http://www.yiwan.com/az/3_0_new_{pag}/'

    response = requests.get(url=url, verify=False)
    selector = parsel.Selector(response.text)
    listli = selector.xpath("//div[@class='r-content softlist']/ul/li")
    for li in listli:
        name = li.xpath("./div[@class='softlist-t']/h3[@class='softlist-t2']/a/text()").get()
        id = li.xpath("./div[@class='softlist-download']/a/@href").re("game/(.*?)/")[0]
        xqlj = "http://www.yiwan.com/" + li.xpath("./div[@class='softlist-download']/a/@href").get()
        res = requests.get(url=xqlj)
        sel = parsel.Selector(res.text)
        downurl = sel.xpath("//div[@class='gi_r']/a/@href").get().strip("\n")
        if downurl == "javascript:;":
            downurl = ""
        tag = li.xpath("./div[@class='softlist-t']/p[@class='softlist-t4']//a/text()").getall()
        # tag = []
        # for tag in tags:
        #     tag.apped(tag)
        memo = li.xpath("./div[@class='softlist-c']/text()").get().strip("\n")
        print(name, id, tag, memo, downurl)
        with open('易玩角色扮演.csv', 'a', encoding='utf-8') as f:
            te = f'{name},{id},{str(tag).strip("[").strip("]").replace(",", ".")},{memo},{downurl}'
            f.write(te)
            f.write('\n')