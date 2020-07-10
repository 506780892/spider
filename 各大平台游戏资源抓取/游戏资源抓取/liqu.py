import requests, parsel, re

# 厉趣
with open('厉趣传奇.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"id"},{"标签"},{"简介"},{"下载地址"}'
    f.write(biaoti)
    f.write('\n')

for pag in range(1, 11):
    url = f'https://s.liqucn.com/s.php?table_flag=app&urlos=&words=%E4%BC%A0%E5%A5%87&page={pag}'

    response = requests.get(url=url)
    selector = parsel.Selector(response.text)
    sel_list = selector.xpath("//div[@class='main']//div[@class='sear_app']/dl")
    for sel in sel_list:
        # name = sel.xpath("./dd/h3/a/text()").get() + sel.xpath("./dd/h3/a/i/text()").get()
        memo = sel.xpath("./dd/p[2]/text()").get()
        tag = sel.xpath("./dd/p/em/text()").get()
        href = sel.xpath("./dd/div[@class='sapp_version']/a/@href").get()
        # id = sel.xpath("./dd/div[@class='sapp_version']/a/@href").re("\w+/(.*?).shtml")[0]
        down_url = parsel.Selector(requests.get(url=href).text).xpath("//div[@class='info_download']//div[@class='apk_btn']/a/@href").get()
        name = parsel.Selector(requests.get(url=href).text).xpath("//div[@class='info_box']//div[@class='info_con']/h1/text()").get()
        id = re.findall("id=(.*?)&", down_url)[0]
        print(name, id, tag, memo, down_url)
        with open('厉趣传奇.csv', 'a', encoding='utf-8') as f:
            te = f'{name},{id},{tag},{memo},{down_url}'
            f.write(te)
            f.write('\n')
