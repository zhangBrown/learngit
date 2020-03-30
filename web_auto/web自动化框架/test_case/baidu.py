from selenium import webdriver
from time import sleep
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(10)
        self.dr.get("http://www.baidu.com")

    def test_something(self):
        self.dr.find_element_by_id("kw").send_keys("unittest")
        self.dr.find_element_by_id("su").click()
        sleep(3)
        title = self.dr.title
        self.assertEqual(title,"unittest_百度搜索")

    def tearDown(self):
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
