import requests
import parsel
import concurrent.futures


def xsSpilder(url):
    response = requests.get(url=url)
    selector = parsel.Selector(response.text)
    # [9:209:]提取前200章小说的url [0:9]是最近更新
    xsurls = selector.css('#list > dl > dd a::attr(href)')[9:209].getall()
    names = selector.css('#list > dl > dd a::text')[9:209].getall()
    # 返回下载小说url列表，小说章节列表
    return [xsurls, names]


def Fiction(url, name):
    response = requests.get(url=url)
    selector = parsel.Selector(response.text)
    text = selector.css('#content p::text').getall()
    # 提取小说内容
    for te in text:
        savedate(te, name)
        # print(te)


def savedate(te, name):
    with open('D:\\万古神帝\\' + name + '.text', 'a', encoding='utf-8') as fp:
        fp.write(te.strip())
        fp.write('\n')
        fp.write('\n')


if __name__ == '__main__':
    # 小说目录url
    url = 'https://www.biquge5200.cc/8_8187/'
    urls = xsSpilder(url)[0]
    names = xsSpilder(url)[1]
    # 如果利用 with 上下文管理器，它会自动关闭线程池。max_workers最大线程数4
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # map会阻塞主线程，等待所有子线程结束，返回 result，如果子线程有报错，也会返回报错信息。
        # 所以这是一个有了所有线程结果的results，下面的打印就不会有阻塞了。
        results = executor.map(Fiction, [urls], [names])
        for url, name in zip(urls, names):
            Fiction(url, name)
