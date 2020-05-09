import requests
import parsel


url_get = 'https://github.com/session'
url_post = 'https://github.com/session'

headers = {

    'Referer': 'https://github.com/login',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
}
# 维持会话
session = requests.Session()
# 获取表单参数
response = session.get(url=url_get)
selector = parsel.Selector(response.text)
authenticity_token = selector.xpath('//input[@name="authenticity_token"]/@value').get()
webauthn_support = selector.xpath('//input[@name="webauthn-support"]/@value').get()
webauthn_iuvpaa_support = selector.xpath('//input[@name="webauthn-iuvpaa-support"]/@value').get()
timestamp_secret = selector.xpath('//input[@name="timestamp_secret"]/@value').get()

data = {
    'commit': 'Sign in',
    'authenticity_token': f'{authenticity_token}',
    'ga_id': '1233370443.1589016542',
    'login': 'username',  # 账号
    'password': 'password',       # 密码
    'webauthn-support': f'{webauthn_support}',
    'webauthn-iuvpaa-support': f'{webauthn_iuvpaa_support}',
    'return_to': '',
    'required_field_947c': '',
    'timestamp': '1589016536084',
    'timestamp_secret': f'{timestamp_secret}',

}

# 模拟登陆
response = session.post(url=url_post, headers=headers, data=data)
print(data)

with open('github.html', mode='wb') as f:
    f.write(response.content)
