import time
from selenium import webdriver

class YunSpider(object):

    def __init__(self, url):
        # 网址
        self.url = url
        # 初始化浏览器
        self.driver = webdriver.Chrome()

    def getContent(self):

        # 打开网址
        self.driver.get(self.url)
        # 切入框内
        self.driver.switch_to.frame(0)
        # 提取5页的评论
        for n in range(5):
            # 下拉混动条
            js = 'window.scrollBy(0,8000)'
            self.driver.execute_script(js)

            time.sleep(1)

            # 选元素
            elememts = self.driver.find_elements_by_xpath('//div[@class="cmmts j-flag"]//div[@class="cntwrap"]')
            # 循环遍历
            for text in elememts:
                result = text.find_element_by_xpath('.//div[@class="cnt f-brk"]').text
                print(result)
                YunSpider.saveFile(result)

            # 翻页
            self.driver.find_element_by_partial_link_text('下一').click()
            time.sleep(1)  # 暂停1s

    @staticmethod
    def saveFile(data):
        with open('Yun.txt', 'a', encoding='utf-8') as fp:
            fp.write(data+'\n')

    # 在对象销毁的时候自动执行这个魔术方法 引用计数为0
    def quit(self):
        # 退出
        self.driver.quit()
if __name__ == '__main__':
    # 歌曲处处吻
    url = 'https://music.163.com/#/song?id=316686'

    yunspider = YunSpider(url)
    yunspider.getContent()
    yunspider.quit()