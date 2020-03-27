# -*- coding: utf-8 -*-
import sys, os
sys.path.append("/home/zhangweibin/api_auto")

import json
import requests
from public.Log_method import Logger
from public.operation_Excel import OperExcel

loger = Logger("req_api", file_dir="/home/zhangweibin/api_auto/data/test.log")


class RunMethod:
    @staticmethod
    def run_main(listdata):
        """调试用"""

        # loger.debug("传入的数据为%s" % listdata)
        li = []

        for i in listdata:
            method = i["method"]
            url = i["url"]
            
            headers = eval(i["headers"])
            data = eval(i["data"])

            loger.debug("请求参数 [url]=%s [param]=%s [headers]=%s" % (url, data, headers)) 
            if method == "get":
                res = requests.get(url=url, params=data, headers=headers, verify=False)
            elif method == "post":
                res = requests.post(url=url, data=data, headers=headers)
            else:
                res = requests.put(url=url, data=data, headers=headers)

            res = res.json()
            res = json.dumps(res, ensure_ascii=False)

            li.append(res)
        return li

    @staticmethod
    def run_test(method, url, data, headers):
        """测试用例用"""

        if method == "get":
            res = requests.get(url=url, params=data, headers=headers, verify=False)
        elif method == "post":
            res = requests.post(url=url, data=data, headers=headers)
        else:
            res = requests.put(url=url, data=data, headers=headers)

        res = res.json()
        return json.dumps(res, ensure_ascii=False)


if __name__ == '__main__':

    wbs = OperExcel().read()
    run = RunMethod()
    data = run.run_main(wbs)
    for i in data:
        print(i)
