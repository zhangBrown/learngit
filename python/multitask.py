import threading
import time


def eat(a):
    for i in range(5):
        print(a)
        print("%s吃饭......" % i)
        time.sleep(0.5)


def run():
    for i in range(5):
        print("%s运动......%s" % (i, threading.current_thread()))
        time.sleep(0.5)

if __name__ == '__main__':
    thread_list = len(threading.enumerate())
    print("当前线程数量为%s" % thread_list)

    thread_eat = threading.Thread(target=eat, args=(10,))
    thread_run = threading.Thread(target=run)
    # 设置子线程守护
    thread_eat.setDaemon(True)
    thread_run.setDaemon(True)
    thread_eat.start()
    # thread_eat.join()  # 优先执行
    """加锁
    lock1 = threading.Lock()
    lock1.acquire()
    xxx
    lock1.release()
    """
    thread_run.start()

    time.sleep(1)
    print("主线程结束")
    exit()