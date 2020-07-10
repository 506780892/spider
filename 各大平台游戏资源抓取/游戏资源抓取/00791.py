import requests
import parsel

# 00791(腾讯)
url = 'https://www.00791.com/chuanqishouyou/'
with open('00791传奇手游.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"id"},{"厂商"},{"简介"},{"下载地址"}'
    f.write(biaoti)
    f.write('\n')

response = requests.get(url=url)
response.encoding = "utf-8"
selector = parsel.Selector(response.text)
data = selector.xpath('//ul[@class="ranking-game ranking-list"]/li/div[@class="gameInfo"]')
for dat in data:
    name = dat.xpath("./em/a/text()").get()
    apkurl = "https://www.00791.com/" + dat.xpath("./em/a/@href").get()
    res = requests.get(url=apkurl)
    res = parsel.Selector(res.text).xpath('//div[@class="des"]//a/@href').get()
    if res != "/url.php?url=":
        xiazai = "https://www.00791.com/" + res
    else:
        xiazai = ""
    id = dat.xpath("./em/a/@href").re("app/(.*?).html")[0]
    authorName = dat.xpath(".//p/text()").get()
    memo =  dat.xpath(".//p[@class='desc']//text()").get().replace(",", ".")
    print(name, id, authorName, memo, xiazai)
    with open('00791传奇手游.csv', 'a', encoding='utf-8') as f:
        te = f'{name},{id},{authorName},{memo},{xiazai}'
        f.write(te)
        f.write('\n')

