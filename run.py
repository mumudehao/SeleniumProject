import os

import pytest

if __name__ == '__main__':

    # 执行用例获得测试数据 数据目录
    pytest.main(['-s','-v','./testCase/testCase.py','--alluredir','./testCase/allureReport'])
    print('sss')
    # 生成测试报告 找到测试数据 生成测试报告目录
    os.system('allure generate ./testCase/allureReport -o ./testCase/reports')