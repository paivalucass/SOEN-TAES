def choose_num(x, y):
    if x > y:
        return -1
    for num in range(y, x-1, -1):
        if num % 2 == 0:
            return num
    return -1
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(choose_num(12, 15), 14)

    def test2(self):
        self.assertEqual(choose_num(13, 12), -1)

if __name__ == '__main__':
    unittest.main()