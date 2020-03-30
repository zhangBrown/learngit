# 协程的使用
import gevent
import time
import urllib.request
from gevent import monkey
monkey.patch_all()


def work1():
    while True:
        print("执行任务1")
        time.sleep(0.5)


def work2():
    while True:
        print("执行任务2")
        time.sleep(0.5)


def down_img(url, file_name):
    try:
        res = urllib.request.urlopen(url)

        with open(file_name, "wb") as file:
            while True:
                data = res.read(1024)
                if data:
                    file.write(data)
                else:
                    break
    except Exception as e:
        print("%s下载失败" % file_name, e)
    else:
        print("%s下载成功" % file_name)


def main():
    url = "https://www.baidu.com/"
    gevent.joinall([
        gevent.spawn(down_img, url, "1.png"),
    ])

if __name__ == '__main__':
    # p1 = gevent.spawn(work1)
    # p2 = gevent.spawn(work2)
    #
    # p1.join()
    # p2.join()
    main()