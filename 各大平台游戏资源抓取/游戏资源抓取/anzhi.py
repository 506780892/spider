import requests
import parsel


with open('anzhijsby.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"包名"},{"简介"},{"id"},{"下载二维码"}'
    f.write(biaoti)
    f.write('\n')

for pag in range(1, 18):
    url = f'http://www.anzhi.com/tsort_76_21_{pag}_hot.html'

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=f178f3dc255087b1c0da35c6b6fec523; UM_distinctid=172ff6fe6651b8-0332509d14b6d9-335f4878-100200-172ff6fe66733f; Hm_lvt_b27c6e108bfe7b55832e8112042646d8=1593423423; CNZZDATA3216547=cnzz_eid%3D924071803-1593423336-%26ntime%3D1593671451; Hm_lpvt_b27c6e108bfe7b55832e8112042646d8=1593676477; CKISP=667785a44906b70ed0e85480e46f74f5%7C1593677168',
        'Host': 'www.anzhi.com',
        'Referer': 'http://www.anzhi.com/tsort_229_21_1_hot.html',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3765.400 QQBrowser/10.6.4153.400',

    }

    response = requests.get(url=url)
    selector = parsel.Selector(response.text)
    title = selector.xpath('//div[@class="app_list border_three"]//li//div[1]//a/@title')
    href = selector.xpath('//div[@class="app_list border_three"]//li//div[1]//@href').re("_(.*?).html")
    Introduction = selector.xpath('//div[@class="app_list border_three"]//li//div//p//text()')
    apkids = selector.xpath('//div[@class="app_list border_three"]//li//div//a//@onclick').re("\((.*?)\)")
    apkimgs = selector.xpath('//div[@class="app_list border_three"]//li//div//div//@rel')

    for (name, pkgid, content, apkid, apkimg) in zip(title, href, Introduction, apkids, apkimgs):
        print(name.get(), pkgid, content.get().replace(",", "."), apkid, apkimg.get())
        with open('anzhijsby.csv', 'a', encoding='utf-8') as f:
            te = f'{name.get()},{pkgid},{content.get().replace(",", ".")},{apkid},{ apkimg.get()}'
            f.write(te)
            f.write('\n')
