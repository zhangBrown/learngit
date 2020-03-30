# print打印
print("hello 练习")
# input输入 接收用户输入信息
admin = input("请输入账号")
print(admin)
# 引号和注释
'''
多行注释    # 单行注释
'''
# if语句 if...elif...else
mark = 72
if mark >= 80:
    print("优秀")
elif mark >= 60:
    print("及格")
else:
    print("不及格")
# for语句循环
for i in "hello world":
    print(i)  # 输出单个字母
fruits = ['banana','apple','orange']  # 数组
for fruit in fruits:
    print(fruit)  # 输出每一种水果
for i in range(1,10,2):
    print(i)  # 输出13579
# 数组与字典
list = [1,2,3,4]  # 数组
print(list[0])   # 0是第一项

list[0] = 5   # 直接修改第一项

list.append(6)   # 增加项
print(list)
# 字典 一个key对应一个value key：value  不同项之间用逗号
dict = {"name":"zhang",'password':123456}
print(dict.keys())
print(dict.values())

# 函数、类、方法
def add(a=1,b=2):  # 函数：设置默认参数
    return a + b
print(add(3,5))

class A():  # 类
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    def add(self):
        return self.a + self.b
count = A(1,2)
print(count.add())

#类的继承
class A():
    def add(self,a,b):
        return a + b
class B(A):
    def sub(self,a,b):
        return a-b
print(B().add(2,4))
# 模组import from...import...
import time
print(time.ctime())  # 获取当前时间
time.sleep(2)  # 休眠2秒

# 捕捉异常
try:
    aa = "异常测试"
    print(aa)
except Exception as msg:
    print(msg)
else:  #finally 不管是否异常都被执行
    print("没有异常")









