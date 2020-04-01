import unittest
from app_auto.public.Log_method import Logger
import os
from app_auto.public.method import *


login_logger = Logger("work_order1", file_dir="D:\python\\app_auto\data\\PiKa.log")
os.system("adb connect 127.0.0.1:62001")
d = u2.connect("127.0.0.1:62001")


class MyTestCase(unittest.TestCase):
    def setUp(self):
        d.healthcheck()
        d.app_start("com.pikachuclientproject")
        d.watcher("update").when("全新版本").when("忽略").click()
        sleep(2)
        d.watcher.run()
        sleep(4)

        login()

        sleep(3)
        d.swipe(0.5, 0.8, 0.5, 0.4)
        d(text="状态").down(text="待分配").right(text="待受理").click()
        d(text="重置").right(text="确定").click()
        d.click(0.5, 0.25)
        sleep(2)

    def tearDown(self):
        d.app_stop("com.pikachuclientproject")
        d.service("uiautomator").stop()
        d.watcher.remove("update")
        sleep(3)

    def test_01(self):
        """待受理工单-转派"""

        d(text="转派").click()
        sleep(2)
        d(text="testuser3").click()
        sleep(2)
        d(text="确定").left(text="取消").click()
        sleep(2)
        d(text="testuser3").click()
        sleep(2)
        d(text="确定").click()
        sleep(1)
        self.assertTrue(res_ass(d(text="转派成功")), "转派成功----fail")
        sleep(2)
        d.swipe(0.5, 0.2, 0.5, 0.8)
        sleep(2)
        self.assertTrue(res_ass(d(text="待受理")), "验证成功----fail")

    def test_02(self):
        """待受理工单-受理"""

        d(text="受理").click()
        d(text="取消").click()
        d(text="受理").click()
        d(text="确定").click()
        sleep(1)
        self.assertTrue(res_ass(d(text="受理成功")), "待受理工单受理成功----fail")
        sleep(2)
        self.assertTrue(res_ass(d(text="处理中")), "验证成功----fail")

if __name__ == '__main__':
    unittest.main()
