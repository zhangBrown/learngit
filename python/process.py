import multiprocessing
import time
import os


def work(a):
    # 进程
    print("敲你妈", a, multiprocessing.current_process().pid)
    print(os.getpid())
    print(os.getppid())


def write(queue):
    # 队列
    for i in range(10):

        if queue.full():
            print("不能写了，满了")
            break

        queue.put(i)
        print("写入", i)
        time.sleep(0.5)


def read(queue):

    while True:

        if queue.qsize() == 0:
            print("为空了")
            break

        value = queue.get()
        print("读取", value)


def download():
    print("正在下载。。。。。")
    time.sleep(0.5)


if __name__ == '__main__':
    # queue1 = multiprocessing.Queue(5)
    # write_1 = multiprocessing.Process(target=write, args=(queue1,))
    # # process_1.daemon = True  # 守护主进程
    # read_1 = multiprocessing.Process(target=read, args=(queue1,))
    #
    # write_1.start()
    # write_1.join()
    #
    # read_1.start()

    # 进程池及进程池的队列
    pool = multiprocessing.Pool(3)
    queue2 = multiprocessing.Manager().Queue(3)

    write_pool = pool.apply_async(write, (queue2,))
    write_pool.wait()
    pool.apply_async(read, (queue2,))

    # for i in range(10):
    #     # pool.apply(download)
    #     pool.apply_async(download)
    #
    pool.close()
    pool.join()