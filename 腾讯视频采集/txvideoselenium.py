from selenium import webdriver
import sys
import you_get

driver = webdriver.Chrome()
driver.get("https://v.qq.com/detail/o/ohd0q2hnrsgjzoz.html")
element = driver.find_element_by_class_name("s1")
# 点击展开更多
element.click()
# 使用xpath提取所有需要下载的url
urls = driver.find_elements_by_xpath("//div[@class='mod_row mod_row_episode']/div/div[2]//span[@class='item item_three']/a")
# print(urls)
# 将需要下载的视频地址放进列表
url_list = []
for url in urls:
    # 提取href属性值
    url = url.get_attribute("href")
    # 将url添加到列表
    url_list.append(url)
# print(url_list)

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

