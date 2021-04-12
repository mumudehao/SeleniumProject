import pytest
from time import sleep
from selenium import webdriver
from ddt import ddt,file_data,data
from pageObject.loginPage import LoginPage
from pageObject.indexPage import IndexPage
from utils.yamlReader import loadyaml, YamlReader


class TestDemo:

    def setup_class(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.ip = IndexPage(cls.driver)

    def teardown_class(cls) -> None:
        sleep(3)
        cls.driver.quit()

    # LoginPage 测试用例实现
    @pytest.mark.parametrize('udata',YamlReader('./config/user.yaml').data)
    def test_1_login(self,udata):
        self.lp.login(udata['userName'],udata['passwd'])
        sleep(3)

    # IndexPage 测试用例实现
    @pytest.mark.parametrize('utxt',YamlReader('./config/searchdata.yaml').data)
    def test_2_search(self,utxt):
        print(utxt,1)
        self.ip.search(utxt['txt'])
        sleep(3)

if __name__ == '__main__':
    import os
    # 执行用例获得测试数据 数据目录
    pytest.main(['-s','-v','testCase.py','--alluredir','./allureReport'])
    print('sss')
    # 生成测试报告 找到测试数据 生成测试报告目录
    os.system('allure generate ./allureReport -o ./reports')