'''
鼠标操作常用方法:perform()执行所有储存的行为  context_click()右击  double_click()
双击 drag_and_drop(source,target)拖动 move_to_element()鼠标悬停
都是先定位赋值再执行鼠标事件
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(5)
        self.dr.get("http://www.baidu.com")

    def test_something(self):
        above = self.dr.find_element_by_link_text("设置")
        ActionChains(self.dr).move_to_element(above).perform()
        sleep(2)
        self.dr.find_element_by_link_text("搜素设置").click()
        sleep(2)
        text = self.dr.find_element_by_xpath("//div[@id='gxszButton']/a[1]").text
        self.assertEqual(text,"保存设置")

if __name__ == '__main__':
    unittest.main()
