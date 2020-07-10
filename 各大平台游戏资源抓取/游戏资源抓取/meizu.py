import requests
import json

with open('meizuxx.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"简介"},{"包名"},{"ID"},{"类型"},{"发行公司"},{"下载地址"}'
    f.write(biaoti)
    f.write('\n')
url = 'https://api-game.meizu.com/games/public/seek?os=28&vc=99900000&dataVcode=99900000&q=%E4%BB%99%E4%BE%A0&product=gamesexpand&start=0&max=10&searchId=7778fb58c8d2718381498c5b89fa9813dd837442&timestamp=1593506256130'
response = requests.get(url=url)
json_data = json.loads(response.text)
# print(json_data)
data = json_data['value']['data']
print(data)
for dat in data:
    name = dat.get('name')
    recommend_desc = dat.get('recommend_desc').replace(",", ".")
    id = dat.get('id')
    package_name = dat.get('package_name')
    category_name = dat.get('category_name')
    publisher = dat.get('publisher')
    # 获取apk下载地址
    dow_url = f'https://api-game.meizu.com/games/public/download/expand/url?os=28&vc=99900000&dataVcode=99900000&package_name={package_name}&game_id={id}&timestamp=1593505618010&auth_time=6000'
    res = requests.get(url=dow_url).json()
    apkurl = res.get('value')
    print(name, recommend_desc, package_name, id, category_name, publisher, apkurl)
    with open('meizuxx.csv', 'a', encoding='utf-8') as f:
        te = f'{name},{recommend_desc},{package_name},{id},{category_name},{publisher},{apkurl}'
        f.write(te)
        f.write('\n')
