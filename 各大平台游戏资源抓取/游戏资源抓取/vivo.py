import requests
import json

# vivo游戏中心
with open('vivomh.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"简介"},{"包名"},{"ID"},{"下载地址"},{"类型"}'
    f.write(biaoti)
    f.write('\n')
for pag in range(1, 6):
    url = f'https://game.vivo.com.cn/api/searchGame?pageIndex={pag}&word=%E9%AD%94%E5%B9%BB&platformVersion=&reqChannel=h5'
    response = requests.get(url=url)
    json_data = json.loads(response.text)
    data = json_data['data']['games']
    print(type(data))
    print(data)
    for dat in data:
        name =dat.get('name')
        recommend_desc = dat.get('recommend_desc').replace(",", ".")
        apkurl = dat.get('apkurl')
        id = dat.get('id')
        pkgName = dat.get('pkgName')
        gameTag = dat.get('gameTag')
        # print(data)
        print(name, recommend_desc, pkgName, id, gameTag, apkurl)
        with open('vivomh.csv', 'a', encoding='utf-8') as f:
            te = f'{name},{recommend_desc},{pkgName},{id},{apkurl},{gameTag}'
            f.write(te)
            f.write('\n')
