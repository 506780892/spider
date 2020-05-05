import requests
import json
import time

url = 'https://aweme-hl.snssdk.com/aweme/v1/feed/?&pull_type=2&device_type=HD1900&device_platform=android&version_code=290&app_name=douyin_lite&cdid=f025474d-7ce8-4bb7-9ad2-307fcee2f98f&os_version=5.1.1&channel=tengxun'
'''
可以随机获取每日抖音推荐视频
使用的url是删除可删除参数后
url = 'https://aweme-hl.snssdk.com/aweme/v1/feed/?type=0&max_cursor=0&min_cursor=-1&count=6&volume=0.7333333333333333&pull_type=2&need_relieve_aweme=0&filter_warn=0&req_from&cached_item_num=8&last_ad_show_interval=4&ts=1588479968&app_type=lite&os_api=22&device_type=HD1900&device_platform=android&ssmix=a&iid=2911141248643918&manifest_version_code=290&dpi=320&uuid=865166020453745&version_code=290&app_name=douyin_lite&cdid=f025474d-7ce8-4bb7-9ad2-307fcee2f98f&version_name=2.9.0&openudid=9cb9ccd698541e15&device_id=69427436699&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=OnePlus&ac=wifi&update_version_code=2900&aid=2329&channel=xiaomi&_rticket=1588479968494&as=a111111111111111111111&cp=a000000000000000000000&app_type=lite&os_api=22&device_type=HD1900&device_platform=android&ssmix=a&iid=2911141248643918&manifest_version_code=290&dpi=320&uuid=865166020453745&version_code=290&app_name=douyin_lite&cdid=f025474d-7ce8-4bb7-9ad2-307fcee2f98f&version_name=2.9.0&openudid=9cb9ccd698541e15&device_id=69427436699&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=OnePlus&ac=wifi&update_version_code=2900&aid=2329&channel=xiaomi(渠道不可少)&_rticket=1588479968494&as=a111111111111111111111&cp=a000000000000000000000&mas HTTP/1.1'

'''
header = {

    'User-Agent': 'com.ss.android.ugc.aweme.lite/220 (Linux; U; Android 5.1.1; zh_CN; MT2-L05; Build/LMY47V; Cronet/58.0.2991.0)'

}

response = requests.get(url=url, headers=header, verify=False)

content = json.loads(response.text)
count = 0
for i in content["aweme_list"]:
    count += 1
    print('-' * 48, count, '-' * 48)
    print('文章标题:', i['desc'], '发布时间:', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['create_time'])))
    # print('发布时间戳:', i['create_time'])
    print('作者ID:', i['author']['short_id'], '作者名称:', i['author']['nickname'],
          '抖音号:', i['author']['unique_id'], '作者生日:', i['author']['birthday'])
    print('作者头像:', i['author']['avatar_larger']['url_list'][0])
    print('文章url:', i['video']['play_addr']['url_list'][0])
    print('评论数:', i['statistics']['comment_count'], '点赞数:', i['statistics']['digg_count'],
          '下载数:', i['statistics']['download_count'], '分享数:', i['statistics']['share_count'],
          '转发数:', i['statistics']['forward_count'])


    print('-' * 100)


