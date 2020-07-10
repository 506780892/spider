import requests

# 好游快爆
with open('好游快爆即时战斗.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"},{"id"},{"包名"},{"简介"},{"标签"},{"下载地址"},{"version"},{"versioncode"},{"size_byte"}'
    f.write(biaoti)
    f.write('\n')
"""
仙侠（1-7）：https://app.3839.com/cdn/android/hotdownload-home-141-id-237-status-0-size-0-star_begin-0-star_end-10-page-1-level-4.htm
角色扮演（1-167）：https://api.3839app.com/cdn/android/hotdownload-home-141-id-2-status-0-size-0-star_begin-0-star_end-10-page-1-level-4.htm
即时战斗（1-48）：https://app.3839.com/cdn/android/hotdownload-home-141-id-46-status-0-size-0-star_begin-0-star_end-10-page-3-level-4.htm 
"""
for pag in range(1, 49):
    url = f'https://api.3839app.com/cdn/android/hotdownload-home-141-id-2-status-0-size-0-star_begin-0-star_end-10-page-{pag}-level-4.htm'

    response = requests.get(url=url, verify=False).json()
    result = response['result']['data']['list']
    for datas in result:
        data = datas['downinfo']
        tags = datas['tags']
        ta = []
        for tag in tags:
            ta.append(tag.get('title'))
        ta = str(ta).replace(",",".").replace("[","").replace("]","").replace("'","")
        appname = data.get('appname').replace(",", ".")
        id = data.get('id')
        packag = data.get('packag')
        appinfo = data.get('appinfo').strip("\r").strip("\n").strip("\t").replace(",", ".").replace("\r", ".").replace("\n", ".").replace("\t", ".")
        apkurl =data.get('apkurl')
        version =data.get('version')
        versioncode =data.get('versioncode')
        size_byte = data.get('size_byte')
        print(appname, id, packag, appinfo, apkurl, version, versioncode, size_byte)
        with open('好游快爆即时战斗.csv', 'a', encoding='utf-8') as f:
            te = f'{appname},{id},{packag},{appinfo},{ta},{apkurl},{version},{versioncode},{size_byte}'
            f.write(te)
            f.write('\n')
