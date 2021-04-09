import pytest
from result import set_dir
import os




if __name__ == '__main__':
    output_dir = set_dir()

    report_data = os.path.join(output_dir, 'data')
    report_html = os.path.join(output_dir, 'html')
    
    parameter_lt = ['-s', '-q' ,'--alluredir', report_data]
    parameter_lt.append('case/test_demo.py')

    pytest.main(parameter_lt)
    os.system("allure generate --clean {} -o {}".format(report_data, report_html))
    # allure serve ./result/2021-04-08/data/
