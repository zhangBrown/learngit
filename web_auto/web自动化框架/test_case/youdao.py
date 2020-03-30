from selenium import webdriver
from time import sleep
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(10)
        self.dr.get("http://www.so.com")

    def test_something(self):
        self.dr.find_element_by_id("input").send_keys("selenium")
        self.dr.find_element_by_id("search-button").click()
        sleep(2)
        title = self.dr.title
        self.assertEqual(title,"selenium_360搜索")

    def tearDown(self):
        self.dr.close()


if __name__ == '__main__':
    unittest.main()
