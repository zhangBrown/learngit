# -*- coding: utf-8 -*-
import requests
import pytest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from api_pytest.data import get_dt
import json
import allure
from api_pytest.utils.operation_Excel import OperExcel

YUM_FILE, FILE_TYPE = get_dt("test_data.xlsx") 
if FILE_TYPE == "xlsx":
    wbs = OperExcel(filename=YUM_FILE)
    YUM_FILE = wbs.read()

@allure.feature('----feature----')
class TestDemo(object):
    def setup(self):
        self.r = requests.session()

    
    @allure.story('----case_demo1----')
    @pytest.mark.parametrize('query_param', [query_param for query_param in YUM_FILE])
    def test_01(self, query_param):
        except_code = query_param["except"].split("=", 1)[1]
        allure.dynamic.description_html('<h2>{}</h2>'.format(query_param['case_name']))
        
        res = self.send_api(query_param)
        res = json.loads(res)
        assert str(res.get("code"))==except_code

    
    def send_api(self,query_param):
        requests.packages.urllib3.disable_warnings()
        api = query_param["api"]
        
        url = api["url"]
        data = eval(api["params"])
        method = api["method"]
        headers = json.loads(api["headers"])
        
        if method == "GET":
            res = self.r.get(url=url, params=data, headers=headers, verify=False)
        elif method == "POST":        
            res = self.r.post(url=url, data=data, headers=headers)
        else:
            res = self.r.put(url=url, data=data, headers=headers)

        res = res.json()
        return json.dumps(res, ensure_ascii=False)
