def choose_num(x, y):
    if x <= 0 or y <= 0 or type(x) != int or type(y) != int:
        return -1

    max_even = -1

    for num in range(y, x - 1, -1):
        if num % 2 == 0:
            return num
    return -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(12, 15), 14)
        self.assertEqual(function_under_test(13, 12), -1)

if __name__ == '__main__':
    unittest.main()