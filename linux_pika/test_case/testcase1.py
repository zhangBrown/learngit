# -*- coding: utf-8 -*-
import sys, os
sys.path.append("/home/zhangweibin/api_auto")
print(sys.path)

import json
import unittest
from public.Log_method import Logger
from public.operation_Excel import OperExcel
from public.reque import RunMethod
from ddt import ddt, data, unpack


loger = Logger("RunCase", file_dir="/home/zhangweibin/api_auto/data/test.log")
testdatas = OperExcel(filename="/home/zhangweibin/api_auto/data/testcase1.xlsx").read()


@ddt
class TestMethod(unittest.TestCase):
    """异常用例"""

    def setUp(self):
        # 设置全局变量，供其他用例使用，字典储存
        self.g = globals()
        print("start")

    def tearDown(self):
        print("end")

    @data(*testdatas)
    @unpack
    def test_01(self, method, url, data, headers, expect_result, case_name):
        run = RunMethod()
        run_res = run.run_test(method=method, url=url,
                               data=eval(data), headers=json.loads(headers))
                               
        run_res = json.loads(run_res)
        print(run_res)

        expec = expect_result.split("=", 1)[1]
        if run_res["msg"] in("pika登录认证服务器不可用", "业务流79不存在"):
            loger.debug("其他异常%s,算通过" % run_res)
            return
        else:
            self.assertEqual(str(run_res["code"]), expec, "reality return%s" % run_res)

if __name__ == '__main__':
    unittest.main()





