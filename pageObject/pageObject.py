import csv
import time




from common.selenium_driver import logger


class PageObject():
    #初始化
    def __int__(self,driver):
        self.driver = driver

    #查找单个元素
    def findelement(self,*ages):
        return self.driver.findelement(*ages)

    # 查找多个元素
    def findelements(self,*ages):
        return self.driver.findelements(*ages)

    #截图 desc描述
    def getScreen(self,desc):

        t = time.strftime('%Y%m%d%H%M%S', time.localtime())
        # ../screen_shots/登录失败_20210413093816.png
        self.driver.get_screenshot_as_file('../screen_shots/' + str(desc) + '_' + str(t) + '.png')
        # 输出截图日志
        logger.info('截图成功:' + str(desc))

    def getCsvData(self,csv_file):
        f = open(file=csv_file,mode='r',encoding='utf-8-sig')
        result = csv.reader(f)

        return  result

