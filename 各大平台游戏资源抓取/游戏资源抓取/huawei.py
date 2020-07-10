import requests
import json

# 华为应用市场
with open('huaweixx.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"简介"},{"包名"},{"ID"},{"appid"},{"下载地址"},{"类型"}'
    f.write(biaoti)
    f.write('\n')
for pag in range(1,6):
    url = f'https://wap1.hispace.hicloud.com/uowap/index?method=internal.getTabDetail&serviceType=20&reqPageNum={pag}&uri=095e55b7d6c14e928680b7d150bc07bb&maxResults=25&zone=&locale=zh_CN'
    response = requests.get(url=url)
    json_data = json.loads(response.text)
    print(type(json_data))
    dataLists = json_data['layoutData']
    print(dataLists)
    for dataList in dataLists:
        dataList = dataList.get('dataList')
        for data in dataList:
            name =data.get('name')
            memo = data.get('memo').replace(",", ".")
            downurl = data.get('downurl')
            appid = data.get('appid')
            ID = data.get('ID')
            package = data.get('package')
            tagName = data.get('tagName')
            # print(data)
            print(name, memo, package, appid, ID, tagName, downurl)
            with open('huaweixx.csv', 'a', encoding='utf-8') as f:
                biaoti = f'{name},{memo},{package},{ID},{appid},{downurl},{tagName}'
                f.write(biaoti)
                f.write('\n')