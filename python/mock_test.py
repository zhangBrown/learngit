import unittest
from unittest.mock import patch


def add_multiply(x, y):
    he = x + y
    cheng = multiply(x, y)
    return he, cheng


def multiply(x, y):
    cheng = x * y + 1
    return cheng


class TaskCase(unittest.TestCase):
    @patch("mock_test.multiply")  # mock本文件的multiply函数
    def test_01(self, mock_multiply):  # 参数为重命名对象
        x = 3
        y = 5
        mock_multiply.return_value = 15  # mock返回的值
        he, cheng = add_multiply(x, y)
        self.assertEqual(8, he)
        self.assertEqual(15, cheng)


if __name__ == '__main__':
    unittest.main()