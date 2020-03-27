import unittest
from app自动化.public.Log_method import Logger
import os
from app自动化.public.method import *


login_logger = Logger("work_order0", file_dir="D:\python\\app自动化\data\\PiKa.log")
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

        d.swipe_points([(170, 560), (170, 745),
                        (175, 930), (358, 926), (549, 931)], 0.2)
        sleep(3)
        d.xpath("//android.view.View/android.view.View[3]/android.widget.ImageView[1]").click()
        sleep(2)

    def tearDown(self):
        d.app_stop("com.pikachuclientproject")
        d.service("uiautomator").stop()
        d.watchers.remove("update")
        sleep(3)

    def test_01(self):
        """处理中tab"""

        d(text="处理中").click()
        sleep(2)
        d.click(0.5, 0.25)
        sleep(2)
        self.assertTrue(res_ass(d(text="处理中")), "我的工单/处理中----fail")

    def test_02(self):
        """处理完成tab"""

        d(text="处理完成").click()
        sleep(2)
        d.click(0.5, 0.25)
        sleep(2)
        self.assertTrue(res_ass(d(text="处理完成")), "我的工单/处理完成----fail")

    def test_03(self):
        """草稿tab"""

        d(text="草稿").click()
        sleep(2)
        d.click(0.5, 0.25)
        sleep(2)
        self.assertTrue(res_ass(d(text="草稿")), "我的工单/草稿----fail")

    def test_04(self):
        """高筛/项目"""

        d(text="处理中").click()
        sleep(2)
        d.click(685, 165)
        sleep(2)
        # d.xpath("//android.widget.TextView[@text='数据中心']").click()
        d.click(215, 125)
        sleep(2)
        d.xpath("//android.widget.TextView[@text='确定']").click()
        sleep(2)
        self.assertTrue(res_ass(d(text="数据中心")), "我的工单/高筛/项目----fail")

    def test_05(self):
        """高筛/类型"""

        d(text="处理中").click()
        sleep(2)
        d.click(685, 165)
        sleep(2)
        # d.xpath("//android.widget.TextView[@text='数据相关']").click()
        d.click(410, 525)
        sleep(2)
        d.xpath("//android.widget.TextView[@text='确定']").click()
        sleep(2)
        self.assertTrue(res_ass(d(text="数据相关")), "我的工单/高筛/类型----fail")


if __name__ == '__main__':
    unittest.main()
