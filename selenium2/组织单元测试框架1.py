from 网易.calculator import Count
import unittest

class MyTest(unittest.TestCase):
    # 公共开始结束
    def setUp(self):
        print("test start")
    def tearDown(self):
        print("test end")
class TestAdd(MyTest):
    def Test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)
    def Test_add1(self):
        j = Count(3,4)
        self.assertEqual(j.add(),7)
class TestSub(MyTest):
    def test_sub(self):
        j = Count(4,1)
        self.assertEqual(j.sub(),3)
    def test_sub1(self):
        j = Count(5,1)
        self.assertEqual(j.sub(),4)

if __name__ == '__main__':
    unittest.main()
