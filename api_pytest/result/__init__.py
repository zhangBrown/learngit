# -*- coding: utf-8 -*-
import os
import time


# 动态创建一个以日期格式的目录
DIR = time.strftime("%Y-%m-%d")


def set_dir():
    base_dir = os.path.dirname(__file__)
    output_dir = os.path.join(base_dir, DIR)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    return output_dir
