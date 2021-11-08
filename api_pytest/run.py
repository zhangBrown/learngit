import pytest
from result import set_dir
import os


"""
# 参数说明：pytest.main([])
    -s，输出, -q，精简输出
    --clean-alluredir,清除上一次的目录缓存数据
    --alluredir,定制化allure
    ../report/,测试数据集保存目录，可自定义命名
    ../api/upload_api.py, Pytest 测试脚本

"""


if __name__ == '__main__':
    output_dir = set_dir()

    report_data = os.path.join(output_dir, 'data')
    report_html = os.path.join(output_dir, 'html')
    
    parameter_lt = ['-s', '-q' ,'--alluredir', report_data]
    parameter_lt.append('case/test_demo.py')

    pytest.main(parameter_lt)
    os.system("allure generate --clean {} -o {}".format(report_data, report_html))
    # allure serve ./result/2021-04-08/data/
