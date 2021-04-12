#!/usr/bin/python
# _*_ coding:utf-8 _*_
import pytest

def setup_module():
    print('作用于整个模块')

def teardown_module():
    print('作用于关闭模块')

class TestCase2:
    def test_20(self):
        print('TestCase2.test_20')


class TestCase:
    age=121
    def setup_class(self):
        print('类执行前')

    def teardown_class(self):
        print('类执行后 ')

    def setup(self):
        print('方法执行前')
    def teardown(self):
        print('方法执行后 ')

    @pytest.mark.run(order=3)
    @pytest.mark.smoke
    @pytest.mark.skipif(age>18,reason='age>18跳过')
    def test_01(self):
        print('方1')
        assert 1==1

    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    def test_03(self):
        print('方3')
        assert 1==2

    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    @pytest.mark.skip('跳过')
    def test_02(self):
        print('方2')
        assert 1==1




if __name__ == '__main__':
    import os
    pytest.main(['-s','-v','-m','smoke','testPyTest.py','--alluredir','./allureReport'])

    # 生成测试报告 找到测试数据 生成测试报告目录
    os.system('allure generate ./allureReport -o ./reports')
