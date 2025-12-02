def choose_num(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        return -1

    if x <= 0 or y <= 0:
        return -1

    max_even = -1
    for num in range(x, y+1):
        if num % 2 == 0:
            max_even = max(max_even, num)

    return max_even
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(choose_num(12, 15), 14)

    def test_2(self):
        self.assertEqual(choose_num(13, 12), -1)

    def test_3(self):
        self.assertEqual(choose_num(2, 5), 4)

if __name__ == '__main__':
    unittest.main()