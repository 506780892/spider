import requests

# 360手机助手
with open('360mh.csv', 'a', encoding='utf-8') as f:
    biaoti = f'{"名字"}, {"简介"}, {"id"}, {"包名"}, {"baike_name"}, {"发行商"}, {"下载地址"},{"version_code"}, {"version_name"}'
    f.write(biaoti)
    f.write('\n')

for pag in range(1, 17):
    url = f'http://zonghe.m.so.com/api/search/app?q=%E9%AD%94%E5%B9%BB&inp=%E9%AD%94%E5%B9%BB&pq=%E4%BC%A0%E5%A5%87&src=ms_zhushou&ext_filter=31&s_stream_app=1&prepage=shrhis_app&curpage=shbtinput_app&os=22&page={pag}&vc=300070071&v=7.0.71&md=SKW-A0&sn=4.589389937671455&cpu=placeholder&ca1=armeabi-v7a&ca2=armeabi&m=8297b7617f9ffe067d882a1997fc6905&m2=a3a47422c94d8033c879c841335541f3&ch=8967318&ppi=720_1280&startCount=1&re=1&tid=0&cpc=1&snt=-1&nt=1&gender=-1&age=0&theme=2&br=blackshark&s_3pk=1  '

    response = requests.get(url=url).json()
    # 获取推荐信息
    if pag == 1:
        pass
        similar_rec = response['similar_rec']['data']
        for dat in similar_rec:
            name = dat.get('name')
            apkid = dat.get('apkid')
            id = dat.get('id')
            down_url = dat.get('down_url')
            soft_corp_name = dat.get('soft_corp_name').replace(",", ".")
            baike_name = dat.get('baike_name')
            single_word = dat.get('single_word').replace(",", ".")
            version_code = dat.get('version_code')
            version_name = dat.get('version_name')
            print(name, single_word, id, apkid, baike_name, soft_corp_name, down_url, version_code, version_name)
            with open('360mh.csv', 'a', encoding='utf-8') as f:
                te = f'{name}, {single_word}, {id}, {apkid}, {baike_name}, {soft_corp_name}, {down_url},{version_code}, {version_name}'
                f.write(te)
                f.write('\n')
    data = response['data']
    for dat in data:
        name = dat.get('name')
        apkid = dat.get('apkid')
        id = dat.get('id')
        down_url = dat.get('down_url')
        soft_corp_name = dat.get('soft_corp_name').replace(",",".")
        baike_name = dat.get('baike_name')
        single_word = dat.get('single_word').replace(",",".")
        version_code = dat.get('version_code')
        version_name =dat.get('version_name')
        print(name, single_word, id, apkid, baike_name, soft_corp_name, down_url, version_code, version_name)
        with open('360mh.csv', 'a', encoding='utf-8') as f:
            te = f'{name}, {single_word}, {id}, {apkid}, {baike_name}, {soft_corp_name}, {down_url},{version_code}, {version_name}'
            f.write(te)
            f.write('\n')
# print(data)
# print(type(data))