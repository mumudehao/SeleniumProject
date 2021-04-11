'''
    LoginPage类，专门用于实现登录页面对象文件
    主体内容包含：
        1.核心的页面元素
            账号，密码，登录按钮
        2.核心业务流
            用户登录流程
'''

from utils.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage(BasePage):

    url='http://www.baidu.com'

    user = (By.NAME,'account')
    PassWd = (By.NAME,'pwd')
    login_button = (By.XPATH,'')

    # 核心业务流
    def login(self,userName,pwd):
        self.visit()
        self.input_(self.user,userName)
        self.input_(self.PassWd,pwd)
        self.click_(self.login_button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    userName = ''
    passwd = ''
    lp = LoginPage(driver)
    lp.login(userName,passwd)

    driver.quit()