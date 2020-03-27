import unittest
from app自动化.public.Log_method import Logger
import os
from app自动化.public.method import *


login_logger = Logger("work_order3", file_dir="D:\python\\app自动化\data\\PiKa.log")
os.system("adb connect 127.0.0.1:62001")
d = u2.connect("127.0.0.1:62001")


class MyTestCase(unittest.TestCase):
    def setUp(self):
        d.healthcheck()
        d.app_start("com.pikachuclientproject")
        d.watcher("update").when(text="全新版本").click(text="忽略")
        sleep(2)
        d.watchers.run()
        sleep(4)

        login()

        sleep(3)
        d.swipe(0.5, 0.8, 0.5, 0.4)
        d(text="状态").down(text="待分配").down(text="已退回").click()
        d(text="重置").right(text="确定").click()
        sleep(2)
        d(text="全部").click()
        sleep(2)
        d.click(0.5, 0.25)
        sleep(2)

    def tearDown(self):
        d.app_stop("com.pikachuclientproject")
        d.service("uiautomator").stop()
        d.watchers.remove("update")
        sleep(3)

    def test_01(self):
        """已退回工单-撤销退回"""

        d(text="撤销退回").click()
        sleep(2)
        d(text="取消").click()
        sleep(2)
        d(text="撤销退回").click()
        sleep(2)
        d(text="取消").right(text="撤销退回").click()
        sleep(2)
        self.assertTrue(res_ass(d(text="处理中")), "撤销退回成功----fail")

if __name__ == '__main__':
    unittest.main()