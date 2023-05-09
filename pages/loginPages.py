from time import sleep

from selenium.webdriver.common.by import By

from common.selenium_driver import logger
from data.apiURL import Index_URL
from pageObject.pageObject import PageObject

#创建页面继承PageObject

class LoginPage(PageObject):
    #记录需要操作的函数
    unBy = (By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/form/div[1]/div[1]/div/div[1]/div/input')
    pwBy = (By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/form/div[2]/div[1]/div/div[1]/div/input')
    dengBy = (By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/button/span')
    #操作函数
    def login(self,name,password):
        #打开页面
        self.driver.get(Index_URL)

        # 输出到日志
        logger.info('用户名：'+name,'密码'+password)
        #用户名
        self.findelement(*self.unBy).clear()
        self.findelement(*self.unBy).send_keys(name)
        #密码
        self.findelement(*self.pwBy).clear()
        self.findelement(*self.pwBy).send_keys(password)
        #点击登陆
        self.findelement(*self.dengBy).cilk()
        sleep(3)
    #检测对应状态
    def checkLogin(self):
        try:
            self.findelement(*self.unBy).clear()
        except Exception as result:

            logger.info("登陆成功")
            return True

        else:
            logger.info("登陆失败,即将截图")
            self.getScreen('登陆失败')
            return False








