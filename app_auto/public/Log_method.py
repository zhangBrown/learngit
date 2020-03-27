import logging


class Logger:
    def __init__(self,path,clevel=logging.DEBUG,file_dir="test.log",flevel=logging.DEBUG):
        # 创建一个logger命名为mylogger, %(name)s可调用这个名字
        self.mylogger = logging.getLogger(path)
        self.mylogger.setLevel(logging.DEBUG)

        # 定义日志输出格式formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s- %(levelname)s - %(message)s')

        # 创建一个handler，用于写入日志文件,只输出debug级别以上的日志，并调用定义的输出格式
        self.fh = logging.FileHandler(file_dir,encoding="utf-8")

        self.fh.setLevel(clevel)
        self.fh.setFormatter(formatter)

        # 再创建一个handler，用于输出到控制台, 一般不用
        self.ch = logging.StreamHandler()
        self.ch.setLevel(flevel)
        self.ch.setFormatter(formatter)

        # 给我们开始实例化的logger对象添加handler
        self.mylogger.addHandler(self.fh)
        self.mylogger.addHandler(self.ch)

    def debug(self,message):
        self.mylogger.debug(message)

    def error(self,message):
        self.mylogger.error(message)

    def info(self,message):
        self.mylogger.info(message)

if __name__ == "__main__":
    wb = Logger("test")
    wb.error("我爱桃子")
