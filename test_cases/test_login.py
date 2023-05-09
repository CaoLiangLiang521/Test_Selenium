import csv
import unittest
import ddt
from common.myUnit import MyUnit
from pages.loginPages import LoginPage


f = open(file='../data/login.csv',mode='r',encoding='utf-8')
result = csv.reader(f)
for r in result:
    dict = {'name':r[0],'password':r[1],'yq':r[2]}
    list = []
    list.append(dict)

@ddt.ddt
class TestLoginPage(MyUnit):

    @ddt.data(*list)
    def test_01_login(self,ls):
        #初始化页面对象
        lp = LoginPage(self.driver)

        #使用对象调用操作函数
        lp.login(ls['name'],ls['password'])
        #断言
        self.assertEqual(ls['yq'],lp.checkLogin())
        lp.tuiChuLogin()

if __name__ == '__main__':
    unittest.main()


