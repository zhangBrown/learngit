import unittest
from app_auto.public.Log_method import Logger
import os
from app_auto.public.method import *


login_logger = Logger("work_order4", file_dir="D:\python\\app_auto\data\\PiKa.log")
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
        d(text="状态").down(text="处理完成").click()
        d(text="重置").right(text="确定").click()
        sleep(2)
        d(text="全部").click()
        sleep(2)
        d.click(0.5, 0.25)
        sleep(2)

    def tearDown(self):
        d.app_stop("com.pikachuclientproject")
        d.service("uiautomator").stop()
        d.watcher.remove("update")
        sleep(3)

    def test_01(self):
        """处理完成工单-继续处理"""

        d(text="继续受理").click()
        sleep(2)
        d(text="取消").click()
        sleep(2)
        d(text="继续受理").click()
        sleep(2)
        d(text="取消").right(text="继续受理").click()
        sleep(2)
        self.assertTrue(res_ass(d(text="处理中")), "继续处理成功----fail")

if __name__ == '__main__':
    unittest.main()