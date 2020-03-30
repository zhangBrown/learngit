'''
css 通过class属性定位:find_element_by_css_selector(".xx")
    通过id属性定位：find_element_by_css_selector("#xx")
    通过父子关系定位：find_element_by_css_selector("xx>xx")
    通过元素属性定位：find_element_by_css_selector("[属性=xxx]")
'''
from selenium import webdriver
from time import sleep
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(5)  # 隐式等待
        self.dr.get("http://www.youdao.com")
        self.dr.maximize_window()  # 窗口最大
    def test_something(self):
        # self.dr.find_element_by_css_selector("#translateContent").send_keys("selenium")
        self.dr.find_element_by_css_selector("[autocomplete=off]").send_keys("selenium")
        sleep(3)
        self.dr.find_element_by_css_selector("form>button").click()
        sleep(3)
        T = self.dr.find_element_by_css_selector(".keyword").text
        self.assertEqual(T,"selenium")
    def tearDown(self):
        sleep(3)
        self.dr.close()

if __name__ == '__main__':
    unittest.main()
