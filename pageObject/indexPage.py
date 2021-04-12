'''
    index_page 页面对象，实现页面中搜索的功能
'''

from utils.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver

class IndexPage(BasePage):

    url = BasePage.url

    input_el = (By.NAME, 'wd')
    button = (By.ID, 'ai-topsearch')

    # 核心业务
    def search(self,txt):
        self.visit()
        self.input_(self.input_el,txt)
        self.click_(self.button)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    txt = 'shouji'
    ip = IndexPage(driver)
    ip.search(txt)


