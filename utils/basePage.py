'''
    BasePage 类是po中的基类，主要用于提供常用的函数，为页面对象进行服务
    常用函数： 元素定位，输入，点击，等待，关闭。。。。
'''


from selenium import webdriver


class BasePage:

    url='http://39.98.138.157/shopxo/index.php'
    # # 虚构driver对象
    # driver = webdriver.Remote(ip,info)

    # 构造函数
    def __init__(self,driver):
        self.driver=driver

    # 打开浏览器
    def visit(self):
        self.driver.get(self.url)


    # 元素定位
    def locator(self,loc):
        return self.driver.find_element(*loc)

    # 输入
    def input_(self,loc,txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def click_(self,loc):
        self.locator(loc).click()

