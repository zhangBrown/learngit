# 元素定位有很多种，精通了xpath和css就能应对各种定位
'''
xpath 绝对路径定位：通过右键语句复制xpath，即可使用。
      利用元素属性定位：find_element_by_xpath("//input[@id='kw']")
      层级与属性结合：find_element_by_xpath("//span[@id='kw']/input")
'''
from selenium import webdriver
from time import sleep
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(10)  # 隐式等待
        self.dr.get("http://www.baidu.com")
    def test_something(self):
        self.dr.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")
        self.dr.find_element_by_xpath("//span[@class='bg s_btn_wr']/input").click()
        sleep(2)
        title = self.dr.title  # 获取网页标题
        self.assertEqual(title,"selenium_百度搜索")
    def tearDown(self):
        self.dr.close()

if __name__ == '__main__':
    unittest.main()
