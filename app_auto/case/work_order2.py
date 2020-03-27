import unittest
from app自动化.public.Log_method import Logger
import os
from app自动化.public.method import *


login_logger = Logger("work_order2", file_dir="D:\python\\app自动化\data\\PiKa.log")
os.system("adb connect 127.0.0.1:62001")
d = u2.connect("127.0.0.1:62001")
sleep(3)


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
        sleep(1)
        d(text="状态").down(text="待受理").right(text="处理中").click()
        sleep(1)
        d(text="重置").right(text="确定").click()

        sleep(1)
        d.click(0.5, 0.25)
        sleep(2)
        d.xpath("//android.view.View/android.view.View[2]/android.view.View[2]").click()
        sleep(2)
        d.click(641, 419)
        sleep(2)

    def tearDown(self):
        d.app_stop("com.pikachuclientproject")
        d.service("uiautomator").stop()
        d.watchers.remove("update")
        sleep(3)

    def test_01(self):
        """处理中工单--继续处理--查看"""

        d.xpath("//android.view.View/android.view.View[2]/android.view.View[2]").click()
        sleep(1)
        d(text="继续流转").click()
        sleep(1)
        d(textContains="处理步骤").set_text("自动化脚本")
        sleep(1)
        d.click(40, 75)
        sleep(1)
        self.assertTrue(res_ass(d(textContains="确定离开")), "点击返回提示----fail")
        d(text="取消").click()
        sleep(2)
        d(text="选择处理人").click()
        sleep(2)
        d(text="testuser3").click()
        sleep(2)
        d(text="提交").click()
        sleep(2)
        d(text="查看工单").click()
        sleep(2)
        self.assertTrue(res_ass(d(text="待受理")), "验证成功----fail")
        sleep(1)
        d.click(40, 75)
        sleep(2)
        self.assertTrue(res_ass(d(text="待办")), "返回工单列表----fail")

    def test_02(self):
        """处理中工单--继续处理--返回"""

        d.xpath("//android.view.View/android.view.View[2]/android.view.View[2]").click()
        sleep(1)
        d(text="继续流转").click()
        sleep(1)
        d(textContains="处理步骤").set_text("自动化脚本")
        sleep(1)
        d.click(40, 75)
        sleep(1)
        self.assertTrue(res_ass(d(textContains="确定离开")), "点击返回提示----fail")
        d(text="取消").click()
        sleep(2)
        d(text="选择处理人").click()
        sleep(2)
        d(text="testuser3").click()
        sleep(2)
        d(text="提交").click()
        sleep(2)
        d(text="返回列表").click()
        sleep(2)
        d.click(40, 75)
        sleep(2)
        self.assertTrue(res_ass(d(text="主页")), "返回到主页----fail")

    def test_03(self):
        """处理中工单--关闭--查看"""

        d.xpath("//android.view.View/android.view.View[2]/android.view.View[2]").click()
        sleep(1)
        d(text="确认关闭").click()
        sleep(1)
        d(textContains="处理结果").set_text("处理完毕" * 25)
        sleep(2)
        d.click(40, 75)
        sleep(2)
        self.assertTrue(res_ass(d(textContains="确定离开")), "点击返回提示----fail")
        d(text="取消").click()
        sleep(2)
        d(text="提交").click()
        sleep(2)
        d(text="查看工单").click()
        sleep(2)
        self.assertTrue(res_ass(d(text="处理完成")), "验证成功----fail")
        sleep(2)
        d.click(40, 75)
        sleep(2)
        self.assertTrue(res_ass(d(text="待办")), "返回工单列表----fail")

    def test_04(self):
        """处理中工单--关闭--返回"""

        d.xpath("//android.view.View/android.view.View[2]/android.view.View[2]").click()
        sleep(1)
        d(text="确认关闭").click()
        sleep(1)
        d(textContains="处理结果").set_text("处理完毕" * 25)
        sleep(2)
        d.click(40, 75)
        sleep(2)
        self.assertTrue(res_ass(d(textContains="确定离开")), "点击返回提示----fail")
        d(text="取消").click()
        sleep(2)
        d(text="提交").click()
        sleep(2)
        d(text="返回列表").click()
        sleep(2)
        d.click(40, 75)
        sleep(2)
        self.assertTrue(res_ass(d(text="主页")), "返回到主页----fail")

    def test_05(self):
        """处理中工单--退回"""

        d(text="退回").click()
        sleep(2)
        d(textContains="退回原因").set_text("退回" * 50)
        sleep(2)
        d.click(40, 75)
        sleep(2)
        self.assertTrue(res_ass(d(textContains="确定离开")), "点击返回提示----fail")
        d(text="取消").click()
        sleep(2)
        d(text="提交").click()
        sleep(1)
        self.assertTrue(res_ass(d(text="工单已退回")), "退回toast提示----fail")
        sleep(2)
        self.assertTrue(res_ass(d(text="已退回")), "退回工单成功----fail")
        sleep(2)
        d.click(40, 75)
        sleep(2)
        self.assertTrue(res_ass(d(text="待办")), "返回到工单列表----fail")

    def test_06(self):
        """获取回复模板"""

        d.press("back")
        sleep(1)
        d.xpath("//android.view.View/android.view.View[3]/android.widget.ImageView[1]").click()
        sleep(2)
        d.click(420, 735)
        sleep(2)
        d(text="重置").right(text="确定").click()
        d.click(0.5, 0.25)
        sleep(2)
        d.xpath("//android.view.View/android.view.View[2]/android.view.View[2]").click()
        sleep(2)
        d(text="确认关闭").click()
        sleep(2)
        d.xpath("//android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.widget.ImageView[1]").click()
        sleep(2)
        self.assertTrue(res_ass(d(textContains="很长的模板")), "获取回复模板--fail")

if __name__ == '__main__':
    unittest.main()

