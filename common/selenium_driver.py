import logging
from logging import config

from selenium import webdriver

#配置日志输出对象

config.fileConfig('../config/log.conf')
#获取日志输出对象

logger = logging.getLogger()


# 1\获取驱动
def selenium_driver():

    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()

    return driver

if __name__ == '__main__':
    logger.info('ceshiyisi')
