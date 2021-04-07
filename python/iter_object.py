# 自定义迭代对象
class MyIter(object):
    def __init__(self):
        self.item = []

    def __iter__(self):
        iter1 = IterIdeal(self.item)
        return iter1

    def add(self, name):
        self.item.append(name)


class IterIdeal(object):
    def __init__(self, item):
        self.item = item

        self.num = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.num < len(self.item):
            data = self.item[self.num]
            self.num += 1
            return data
        else:
            raise StopIteration


class FbNq(object):
    """斐波那契数列"""
    def __init__(self, num):
        self.num = num
        self.count = 0

        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.count < self.num:
            data = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return data
        else:
            raise StopIteration


def fbnq1(num):
    """生成器的方式"""
    a = 1
    b = 1
    cur_num = 0

    while cur_num < num:
        data = a
        a, b = b, a + b
        cur_num += 1
        xxx = yield data
        if xxx == 1:
            return "返回"


if __name__ == '__main__':
    # iter_obj = MyIter()
    # iter_obj.add("张飞")
    # iter_obj.add("关羽")
    # iter_obj.add("刘备")
    #
    # # for i in iter_obj:
    # #     print(i)
    # test = iter(iter_obj)
    # print(next(test))

    # fbnq = FbNq(10)
    # for i in fbnq:
    #     print(i)

    # 生成器
    # list1 = (i*2 for i in range(5))
    # for i in list1:
    #     print(i)
    fib = fbnq1(5)
    value = next(fib)
    print(value)
    try:
        value = next(fib)
        print(value)
        value = next(fib)
        print(value)

        value = fib.send(1)
        print(value)
    except Exception as e:
        print(e)
