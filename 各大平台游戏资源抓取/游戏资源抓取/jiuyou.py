import requests
import re

with open('jiuyoumh.csv', 'a', encoding='utf-8') as f:
    te = f'{"名字"}, {"id"}, {"标签"}, {"类型"}, {"简介"}, {"pkgId"}, {"pkgName"},{"下载地址"}'
    f.write(te)
    f.write('\n')
for pag in range(1, 13):
    url = f'http://web.9game.cn/game/search/pager?keyword=%E9%AD%94%E5%B9%BB&pageIndex={pag}&_pagelets=layout.game.list '
    headers = {

    'Host': 'web.9game.cn',
    'Connection': 'keep-alive',
    'Accept': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Pagelets': 'layout.game.list',
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh_CN; SKW-A0; Build/LMY47I) cn.ninegame.gamemanager/1252; NineGameClient/android ve/5.1.3.2 si/6e22a024-9d84-4b39-b6d5-b0af2bef794d ch/WM_7120 ss/720x1280 ng/cdc6b760a6c296e75c76573b5a15f6c52f ut/XvMGZfa2ihQDABMszd7KhOf2 nt/wifi',
    'Referer': 'http://web.9game.cn/game/search?pn=%E6%B8%B8%E6%88%8F%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C&keyword=%E4%BC%A0%E5%A5%87&scene=search_result',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
    'Cookie': 'sdksid=0; sidType=2; serviceTicket=0; ucid=0; uuid=6e22a024-9d84-4b39-b6d5-b0af2bef794d; ast=0; st_=1593584464126; st_.sig=zTf3JRA3BAhGyuO7W9phzc2v8hU; ex={%22width%22:360%2C%22height%22:531%2C%22imsi%22:%22460008946762998%22%2C%22mac%22:%2200:81:34:1a:c3:2c%22%2C%22imei%22:%22865166023473898%22}',

    }

    response = requests.get(url=url, headers=headers).json()['script']
    print(response)
    for script in response:
        name = re.findall('name":"(.*?)",', script)
        if name:
            name = name[0]

        id = re.findall('gameId":(.*?),', script)
        if id:
            id = id[0]

        shortName = re.findall('shortName":"(.*?)",', script)
        if shortName:
            shortName = shortName[0]
        else:
            shortName = ""

        category = re.findall('category":"(.*?)",', script)
        if category:
            category = category[0]
        else:
            category = ""

        instruction = re.findall('instruction":"(.*?)",', script)
        if instruction:
            instruction = instruction[0]
        else:
            instruction = ""

        pkgId = re.findall('pkgId":(.*?),', script)
        if pkgId:
            pkgId = pkgId[0]
        else:
            pkgId = ""

        pkgName = re.findall('pkgName":"(.*?)",', script)
        if pkgName:
            pkgName = pkgName[0]
        else:
            pkgName = ""

        downloadUrl = re.findall('downloadUrl":"(.*?)",', script)
        if downloadUrl:
            downloadUrl = downloadUrl[0]
        else:
            downloadUrl = ""
        print(name, id, shortName, category, instruction, pkgId, pkgName)
        with open('jiuyoumh.csv', 'a', encoding='utf-8') as f:
            te = f'{name}, {id}, {shortName}, {category}, {instruction}, {pkgId}, {pkgName},{downloadUrl}'
            f.write(te)
            f.write('\n')
