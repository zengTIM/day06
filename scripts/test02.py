import os
import sys

import pytest

sys.path.append(os.getcwd())


import allure


class Test02():


    @allure.step("新增地址方法")
    def test03(self):
        allure.attach("新增地址被执行", "")
        print("test03被执行")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)#用例级别
    @allure.step("更改地址方法")
    def test04(self):
        allure.attach("更改地址被执行", "")#注释
        print("test04被执行")
    @allure.severity("minor")#用例级别
    def test05(self):
        print("test05被执行")
        with open("./image/abc.png","rb")as f:
            allure.attach("失败原因:",f.read(),allure.attach_type.PNG) #图片加入报告