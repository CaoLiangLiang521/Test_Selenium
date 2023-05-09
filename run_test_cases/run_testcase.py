import unittest

from run_test_cases import HTMLTestRunnerX
from run_test_cases.HTMLTestRunnerX import HTMLTestRunner
from test_cases.test_login import TestLoginPage

#1 获取测试套件


suite = unittest.TestSuite()
#2 添加测试用例集
suite.addTests(unittest.TestLoader.loadTestsFromTestCase(TestLoginPage))
#3 获取html运行器
f = open(file='../reporst/UI自动化报告.html',mode='wb',)
runner = HTMLTestRunner(stream=f,verbosity=3,title='UI自动化测试')
#4 运行生成报告

runner.run(suite)

