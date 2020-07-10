import requests, parsel

# 心愿
with open('心愿角色扮演.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"id"},{"标签"},{"详情页"},{"下载地址"}'
    f.write(biaoti)
    f.write('\n')

for pag in range(1, 101):
    url = f'https://www.wishdown.com/soft/newlist_546_{pag}.html'

    response = requests.get(url=url)
    selctor = parsel.Selector(response.text)
    sel_list = selctor.xpath("//div[@class='matter_left']/ul/li")
    for sel in sel_list:
        name = sel.xpath("./h2/a/text()").get()
        id = sel.xpath("./h2/a/@href").re("/soft/(.*?).html")[0]
        tag = sel.xpath("./em/text()").get()
        href = "https://www.wishdown.com/" + sel.xpath("./h2/a/@href").get()
        res = requests.get(href)
        se = parsel.Selector(res.text).xpath('//*[@id="body"]/div[3]/div[2]/div[2]/div[1]/a[2]/@href').get()
        if se != "javascript:;":
            down_url = parsel.Selector(res.text).xpath('//*[@id="body"]/div[3]/div[2]/div[2]/div[1]/a[2]/@href').get()
        else:
            down_url = ""
        print(name, id, tag, href, down_url)
        with open('心愿角色扮演.csv', 'a', encoding='utf-8') as f:
            te = f'{name},{id},{tag},{href},{down_url}'
            f.write(te)
            f.write('\n')
