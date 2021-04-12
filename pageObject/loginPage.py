'''
    LoginPage类，专门用于实现登录页面对象文件
    主体内容包含：
        1.核心的页面元素
            账号，密码，登录按钮
        2.核心业务流
            用户登录流程
'''
from time import sleep

from utils.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage(BasePage):

    url= BasePage.url + '?s=/index/user/logininfo.html'
    # 页面中关联的元素对象
    user = (By.NAME,'accounts')
    PassWd = (By.NAME,'pwd')
    login_button = (By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')

    # 核心业务流
    def login(self,userName,passwd):
        self.visit()
        self.input_(self.user,userName)
        self.input_(self.PassWd,passwd)
        self.click_(self.login_button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    userName = 'xuzhu666'
    passwd = '123456'
    lp = LoginPage(driver)
    lp.login(userName,passwd)
    sleep(3)
    driver.quit()