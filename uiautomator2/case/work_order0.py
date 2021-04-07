import unittest
from app_auto.public.Log_method import Logger
import os
from app_auto.public.method import *


login_logger = Logger("work_order0", file_dir="D:\python\\app_auto\data\\PiKa.log")
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
        sleep(2)
        d(text="状态").down(text="待分配").click()
        sleep(2)
        d(text="重置").right(text="确定").click()

        d.click(0.5, 0.25)
        sleep(2)

    def tearDown(self):
        d.app_stop("com.pikachuclientproject")
        d.service("uiautomator").stop()
        d.watcher.remove("update")
        sleep(3)

    def test_01(self):
        """待分配工单-添加备注"""

        d.swipe(0.5, 0.5, 0.5, 0.4)
        d(text="工单信息").click()
        d(text="复制").click()
        self.assertTrue(res_ass(d(text="已复制")), "复制工单编号----fail")

        d(text="添加备注").click()
        d(text="填写备注信息").set_text("张" * 100)
        d(text="取消").click()
        self.assertTrue(res_ass(d(textContains="已输入的信息将不会")), "输入内容点击返回显示----fail")
        d(text="取消").click()
        sleep(2)
        self.assertIsNotNone(d(text="填写备注信息"), "取消保留了备注内容----fail")
        d(text="提交").click()
        sleep(1)
        self.assertTrue(res_ass(d(text="添加备注成功")), "添加备注成功----fail")

        sleep(2)
        d.swipe(0.5, 0.5, 0.5, 0.4)
        d(text="工单流转").click()
        sleep(2)
        d(text="全部").click()
        sleep(2)
        self.assertTrue(res_ass(d(text="收起")), "添加备注成功，点击全部显示收起----fail")

    def test_02(self):
        """待分配工单-受理"""

        d(text="受理").click()
        d(text="取消").click()
        d(text="受理").click()
        d(text="确定").click()
        sleep(1)
        self.assertTrue(res_ass(d(text="受理成功")), "待分配工单受理成功----fail")
        sleep(2)
        self.assertTrue(res_ass(d(text="处理中")), "验证受理成功----fail")

    def test_03(self):
        """待分配工单-分配工单"""

        d(text="分配工单").click()
        sleep(2)
        d.swipe(0.5, 0.9, 0.5, 0.1)
        sleep(2)
        if not res_ass(d(text="testuser3")):
            d.swipe(0.5, 0.1, 0.5, 0.9)
        d(text="testuser3").click()
        sleep(2)
        d(text="确定").left(text="取消").click()
        sleep(2)
        d(text="testuser3").click()
        sleep(2)
        d(text="确定").click()
        sleep(1)
        self.assertTrue(res_ass(d(text="分配成功")), "分配成功----fail")
        sleep(3)
        self.assertTrue(res_ass(d(text="待受理")), "验证成功----fail")

if __name__ == '__main__':
    unittest.main()
