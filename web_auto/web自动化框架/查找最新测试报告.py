import os
# 定义文件目录
result_dir = 'D:\\python\\web自动化框架\\report'

list = os.listdir(result_dir)
# 按时间对目录下文件进行排序
list.sort(key=lambda fn: os.path.getatime(result_dir+"\\"+fn))

print(('最新文件为： ' + list[-1]))
file = os.path.join(result_dir, list[-1])
print(file)

