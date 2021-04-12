import unittest
from time import sleep

from selenium import webdriver
from pageObject.LoginPage import LoginPage
from pageObject.indexPage import IndexPage
from ddt import ddt,file_data,data,unpack


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.ip = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../config/user.yaml')
    def test_1_login(self,userName,passwd):
        self.lp.login(userName,passwd)
        sleep(3)

    @data('手机','衣服','1')
    def test_2_search(self,txt):
        self.ip.search(txt)
        sleep(3)


if __name__ == '__main__':
    unittest.main()