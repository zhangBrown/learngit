# -*- coding: utf-8 -*-
import sys, os
sys.path.append("/home/zhangweibin/api_auto")

import requests
from public.login_public import connect_SQL
from public.login_public.get_sign import get_sign
from time import sleep
import time


sign = get_sign()
headers = {"client-sign": sign}


def get_devices():
    url = "http://42.186.57.244:10018/auth/deviceid"

    data = {
        "platform": "android"
    }

    res = requests.get(url, params=data, headers=headers, verify=False)
    return res.json()


def get_pwd():
    deviceid = get_devices()["data"]
    res_time = int(round(time.time() * 1000))

    url = "http://42.186.57.244:10018/auth/captcha"

    data = {'trigger_time': res_time, 'phone_number': '13631289205', 'token': '', 'device_id': deviceid}
    
    res = requests.post(url, data=data, headers=headers)
    res = res.json()
    if res["code"] == -1:
        token = login(deviceid)
        auth_token = deviceid + "##" + token
        return auth_token, token, deviceid
    else:
        return "get_pwd fail"


def login(deviceid):
    run = connect_SQL.ConSql()
    res = run.run_sql("select captcha from PhoneCaptcha order by pcid desc limit 1;")
    pwd = res[0]
    sleep(1)
    
    url = "http://42.186.57.244:10018/auth/login"
    data = {'token': '', 'device_id': deviceid, 'phone_number': '13631289205', 'phone_captcha': pwd}
    res = requests.post(url, data=data, headers=headers)
    res = res.json()
    return res["data"]

if __name__ == '__main__':
    res = get_pwd()
    print(res)
