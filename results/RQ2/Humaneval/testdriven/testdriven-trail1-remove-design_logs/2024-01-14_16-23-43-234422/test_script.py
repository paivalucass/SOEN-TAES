def choose_num(x, y):
    if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0 or x > y:
        return -1
    for i in range(y, x-1, -1):
        if i % 2 == 0:
            return i
    return -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(12, 15), 14)
        self.assertEqual(function_under_test(13, 12), -1)

if __name__ == '__main__':
    unittest.main()