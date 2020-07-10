import requests
import json
import re

# 应用宝
with open('yingyongbao1.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"简介"},{"游戏id"},{"包名"},{"versionName"},{"发行公司"},{"下载地址"}'
    f.write(biaoti)
    f.write('\n')
for pag in range(1, 22):
    start_url = f'https://sj.qq.com/myapp/cate/appList.htm?orgame=2&categoryId=121&pageSize=20&pageContext=60'
    response = requests.get(url=start_url)
    json_data = json.loads(response.text)
    gameList = json_data['obj']
    for game in gameList:
        appName = game.get('appName')
        authorName = game.get('authorName')
        apkUrl = game.get('apkUrl')
        appId = game.get('appId')
        versionName = game.get('versionName')
        editorIntro = game.get('editorIntro')
        pkgName = game.get('pkgName')
        newFeature =game.get('newFeature')
        print(appName, editorIntro, appId, pkgName, versionName, authorName, apkUrl)
        with open('yingyongbao1.csv', 'a', encoding='utf-8') as f:
            te = f'{appName},{editorIntro},{appId},{pkgName},{versionName},{authorName},{apkUrl}'
            f.write(te)
            f.write('\n')




