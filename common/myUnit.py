import unittest
from time import sleep

from common.selenium_driver import selenium_driver


class MyUnit(unittest.TestCase):

    @classmethod
    def setUpClass(self):
       self.driver = selenium_driver()


    @classmethod
    def tearDownClass(self):
        sleep(3)
        self.driver.quit()


