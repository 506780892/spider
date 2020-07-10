import requests
import json
import re

# 小米应用商店
with open('xiaomi1.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"简介"},{"游戏id"},{"包名"},{"预测devAppId"},{"devAppId"},{"发行公司"},{"下载地址"},{"下载地址ssl"},{"标签"}'
    f.write(biaoti)
    f.write('\n')
for pag in range(1, 22):
    start_url = f'https://game.xiaomi.com/api/classify/getCategory?firstCategory=1&secondCategory=&apkSizeMin=0&apkSizeMax=0&language=&network=2&options=&page={pag}&gameSort=1'
    response = requests.get(url=start_url)
    # 将response转换为字典格式
    json_data = json.loads(response.text)
    # print(json_data)
    gameList = json_data['gameList']
    # print(type(gameList))

    for game in gameList:
        displayName = game.get('gameInfo').get('displayName')
        gameId = game.get('gameInfo').get('gameId')
        gameInfoid = game.get('gameInfo').get('devAppId')
        devAppId = str(game.get('devAppId'))
        packageName = game.get('gameInfo').get('packageName')
        publisherName = game.get('gameInfo').get('publisherName')
        gameApk = game.get('gameInfo').get('gameApk')
        gameApkSsl = gameApk = game.get('gameInfo').get('gameApkSsl')
        shortDesc = game.get('detail').get('shortDesc').replace(",", "。").rstrip()
        tags = game.get('tag')
        taglist = []
        for tag in tags:
            tag = tag.get('name')
            taglist.append(tag)
        # print(displayName, shortDesc, gameId, packageName, gameInfoid, devAppId, publisherName, gameApk)

        with open('xiaomi1.csv', 'a', encoding='utf-8') as f:
            biaoti = f'{"名字"},{"简介"},{"游戏id"},{"包名"},{"devAppId"},{"发行公司"},{"下载地址"},{"下载地址ssl"},{"tag"}'
            te = f'{displayName},{shortDesc},{gameId},{packageName},{gameInfoid},{devAppId},{publisherName},{gameApk},{gameApkSsl},{taglist}'
            print(te, devAppId)
            f.write(te)
            f.write('\n')



