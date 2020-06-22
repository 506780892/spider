import requests
import sys
import you_get
import json

start_url = 'https://s.video.qq.com/get_playsource?id=ohd0q2hnrsgjzoz&plat=2&type=4&data_type=2&video_type=106&range=1-26&plname=qq&otype=json&num_mod_cnt=20&callback=_jsonp_2_08b3&_t=1592796657622'
response = requests.get(url=start_url)
# 将字符串前后干扰内容替换
response = response.text.replace("_jsonp_2_08b3(", "")
response = response.replace(")", "")
# 将response转换为字典格式
json_data = json.loads(response)
# 提取videoPlayList内容
videoPlayList = json_data['PlaylistItem']['videoPlayList']
# 将videoPlayList中视频url进行提取
url_list = []
for url in videoPlayList:
    url = url.get('playUrl')
    url_list.append(url)


def download(url, path):
    sys.argv = ['you-get', '-o', path, url]
    you_get.main()


if __name__ == '__main__':
    # 视频输出的位置
    path = 'D:/video'
    # 遍历视频网站的地址
    for url in url_list:
        url = url
        download(url, path)
