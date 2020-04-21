import sys, os
sys.path.append("/home/zhangweibin/api_auto")

import unittest
from public.HTMLTestRunner import HTMLTestReportCN
import time
from public.send_smtp import send_mail


if __name__ == "__main__":

    def main():
        # 定义测试用例的存放路径
        test_dir = "./test_case/"
        # 把测试用例加入 discover 容器(discover(test_dir,"*.py") 把传入的参数路劲文件 加入到容器当中并且返回)
        discover = unittest.defaultTestLoader.discover(test_dir, "*.py")

        # 定义测试报告的存放路径
        testReportDir = "./result/"
        # 定义测试报告的名字（strftime 时间按照规定的字符串格式输出）
        nowTime = time.strftime("%Y-%m-%d%H%M%S", time.localtime())  # time.localtime() 获取当前的系统时间
        fileName = nowTime + ".html"  # 确定测试报告的文件名称以及后缀名 2018-06-14090909.html
        # 定义测试路径和测试报告名字
        testReportDir_FileName = testReportDir + fileName  # 确定测试报告文件具体路劲  ./report/2018-01-18090909.html

        # 打开文件，并赋予可写权限
        fp = open(testReportDir_FileName, "wb")

        # 把测试结果写进测试报告，并装载到HTHMLTestRunner模块
        runner = HTMLTestReportCN(stream=fp, title="自动化测试报告", description="用例执行情况", tester="张伟斌")

        # 运行测试用例
        runner.run(discover)



    main()
    # 找出最新测试报告发送邮件
    receiver = "xxx"
    result_dir = "./result"
    list = os.listdir(result_dir)
    list.sort(reverse=True)
    time = list[0].split(".")[0]

    res_dir = "./result" + "/" + list[0]
    print("最新的测试报告地址为%s"% res_dir)

    send_mail(time, receiver, res_dir)


