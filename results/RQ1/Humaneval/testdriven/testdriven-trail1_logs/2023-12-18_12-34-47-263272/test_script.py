def choose_num(x, y):
    max_even = -1
    if x <= 0 or y <= 0 or x > y:
        return -1
    if x % 2 != 0:
        x += 1
    for i in range(y, x-1, -1):
        if i % 2 == 0 and i > max_even:
            max_even = i
    return max_even
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(12, 15), 14)
        self.assertEqual(function_under_test(13, 12), -1)

if __name__ == '__main__':
    unittest.main()