# -*- coding: utf-8 -*-
import sys, os
sys.path.append("/home/zhangweibin/api_auto")
import json
import unittest
import requests
import time
from public.login_public.get_sign import get_sign
from public.login_public import connect_SQL


sign = get_sign()
headers = {"client-sign": sign}


class TestMethod(unittest.TestCase):
    """其他异常用例"""

    def setUp(self):
        # 设置全局变量，供其他用例使用，字典储存
        self.g = globals()
        self.url = "http://42.186.57.244:10018"
        self.r = requests.session()

    def tearDown(self):
        pass

    def test_01(self):
        """获取设备id-空的设备类型"""
        url = self.url + "/auth/deviceid"
        data = {
                "platform": ""
        }

        res = self.r.get(url, params=data, headers=headers, verify=False)
        res_data = res.json()

        self.assertEqual(res_data["code"], -1, "实际返回%s" % res_data)

    def test_02(self):
        """获取设备id-设备类型错误"""
        url = self.url + "/auth/deviceid"
        data = {
                "platform": "andrid"
        }

        res = self.r.get(url, params=data, headers=headers, verify=False)
        res_data = res.json()

        self.assertEqual(res_data["code"], -1, "实际返回%s" % res_data)

    def test_03(self):
        """获取设备id-正确的设备类型"""
        url = self.url + "/auth/deviceid"
        data = {
                "platform": "ios"
        }
        
        res = self.r.get(url, params=data, headers=headers, verify=False)
        res_data = res.json()
        self.g["deviceid"] = res_data["data"]

        self.assertEqual(res_data["code"], 0, "实际返回%s" % res_data)

    def test_04(self):
        """获取验证码-10位手机号"""
        url = self.url + "/auth/captcha"
        res_time = int(round(time.time() * 1000))
        data = {'trigger_time': res_time, 
                'phone_number': '1363128920', 
                'token': '', 
                'device_id': self.g["deviceid"]}
        
        res = self.r.post(url, data=data, headers=headers)
        res_data = res.json()

        self.assertEqual(res_data["code"], -1, "实际返回%s" % res_data)

    def test_05(self):
        """获取验证码-系统不存在的手机号"""
        url = self.url + "/auth/captcha"
        res_time = int(round(time.time() * 1000))
        data = {'trigger_time': res_time,
                'phone_number': '77777777777',
                'token': '',
                'device_id': self.g["deviceid"]}
        
        res = self.r.post(url, data=data, headers=headers)
        res_data = res.json()

        self.assertEqual(res_data["code"], 6, "实际返回%s" % res_data)

    def test_06(self):
        """获取验证码-正确的手机号"""
        url = self.url + "/auth/captcha"
        res_time = int(round(time.time() * 1000))
        data = {'trigger_time': res_time,
                'phone_number': '66666666666',
                'token': '',
                'device_id': self.g["deviceid"]}
        
        res = self.r.post(url, data=data, headers=headers)
        res_data = res.json()

        self.assertEqual(res_data["code"], -1, "实际返回%s" % res_data)

    def test_07(self):
        """登录-验证码不正确"""
        # run = connect_SQL.ConSql()
        # res = run.run_sql("select captcha from PhoneCaptcha order by pcid desc limit 1;")
        # pwd = res[0]
        pwd = 55555
        url = self.url + "/auth/login"
        data = {'token': '', 'device_id': deviceid, 'phone_number': '66666666666', 'phone_captcha': pwd}
        
        res = self.r.post(url, data=data, headers=headers)
        res_data = res.json()

        self.assertEqual(res_data["code"], -1, "实际返回%s" % res_data)


if __name__ == '__main__':
    unittest.main()





