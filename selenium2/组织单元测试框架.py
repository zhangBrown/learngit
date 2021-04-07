from 网易.calculator import Count
import unittest
# 测试类1
class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test start")
    def test_something(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)
    def test_something1(self):
        j = Count(4,5)
        self.assertEqual(j.add(),9)
    def tearDown(self):
        print("test end")
# 测试类2
class TestSub(unittest.TestCase):
    def setUp(self):
        print("test sub start")
    def test_sub(self):
        j = Count(6,2)
        self.assertEqual(j.sub(),4)
    def test_sub1(self):
        j = Count(7,1)
        self.assertEqual(j.sub(),6)
    def tearDown(self):
        print("test sub end")

# if __name__ == '__main__':
   # unittest.main()
# 构建测试集  一个功能的验证往往需要多个测试用例
suite = unittest.TestSuite()
suite.addTest(TestAdd("test_something1"))
suite.addTest(TestAdd("test_something"))
suite.addTest(TestSub("test_sub"))
suite.addTest(TestSub("test_sub1"))
# 执行测试
runner = unittest.TextTestRunner()
#运行所组装的测试用例
runner.run(suite)
