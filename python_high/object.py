"""封装
class HostItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s占地%s" %(self.name, self.area)

bed = HostItem("席梦思", 4)
chest = HostItem("衣柜", 2)
table = HostItem("餐桌", 1.5)


class Host:
    def __init__(self, host_type, area):
        self.host_type = host_type
        self.area = area
        self.item_list = []
        self.free_area = area

    def __str__(self):
        return "户型是%s，总面积%s，剩余面积%s，拥有家具%s" \
               %(self.host_type, self.area, self.free_area, self.item_list)

    def add_item(self, item):
        if item.area > self.free_area:
            print("太大了，%s添加不了" % item)
            return
        self.item_list.append(item.name)
        self.free_area -= item.area

host = Host("1房", 10)
host.add_item(bed)
host.add_item(table)
host.add_item(chest)
print(host)
"""

"""继承
class Cat1(object):
    def __init__(self, name):
        self.name = name
        # self.name = "Tom"
        print("我来了")

    def __del__(self):
        # 销毁前自动调用,也可以主动调用
        print("我走了")

    def __str__(self):
        # 自定义打印对象内容，必须返回字符串
        return "%s对象内容" % self.name

    def eat(self):
        print("%s吃鱼啦" % self.name)


class Cat2(Cat1):
    def eat(self):
        # 方法的重写，也可以不继承，直接重写
        super().eat()
        print("%s继承并重写" % self.name)
    def wan(self):
        print("%s玩起来" % self.name)

tom = Cat2("Tom")  # dir(tom)查看对象所有属性及方法
tom.eat()
print(tom)
del tom
"""


# 多态-不同的子类对象，调用相同父类方法，产生不同结果
# class Dog:
#     def __init__(self, name):
#         self.name = name
#
#     def game(self):
#         print("%s玩起来" % self.name)
#
#
# class XiaoTian(Dog):
#     def game(self):
#         print("%s飞上天玩" % self.name)
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def game_with_dog(self, dog):
#         print("%s和%s玩起来" %(self.name, dog.name))
#         dog.game()
#
# # dog = Dog("狗")
# dog = XiaoTian("狗")
# person = Person("小明")
# person.game_with_dog(dog)

# 类属性和方法
class Itools:
    # 类属性，计算创建了多少个对象
    count = 0
    instance = None
    init_flg = False

    def __new__(cls, *args, **kwargs):
        """分配空间，返回对象引用"""
        # 单例设计模式-单个实例
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        if Itools.init_flg:
            return
        print("初始化")
        self.name = name
        Itools.count += 1
        Itools.init_flg = True

    @classmethod
    def show_tool_count(cls):
        """类方法"""
        return "创建了%s个对象" % cls.count

    @staticmethod
    def work():
        print("静态方法")

a = Itools("a")
b = Itools("b")
print(Itools.count)
print(Itools.show_tool_count())
# print(a.count)  # 向上查找属性，不建议使用





