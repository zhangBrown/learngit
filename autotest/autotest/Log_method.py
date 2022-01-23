# -*- coding: utf-8 -*-
import logging


class Logger:
    def __init__(self, path, clevel=logging.DEBUG, file_dir="/Users/zhangweibin/gitproject/learngit/autotest/debug.log", flevel=logging.DEBUG):
        self.mylogger = logging.getLogger(path)
        self.mylogger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s- %(levelname)s - %(message)s')
        self.fh = logging.FileHandler(filename=file_dir, encoding="utf-8")
        self.fh.setLevel(clevel)
        self.fh.setFormatter(formatter)

        self.ch = logging.StreamHandler()
        self.ch.setLevel(flevel)
        self.ch.setFormatter(formatter)

        self.mylogger.addHandler(self.fh)
        self.mylogger.addHandler(self.ch)

    def debug(self, message):
        self.mylogger.debug(message)

    def error(self, message):
        self.mylogger.error(message)

    def info(self, message):
        self.mylogger.info(message)


if __name__ == "__main__":
    wb = Logger("test")
    wb.error("loveless")
