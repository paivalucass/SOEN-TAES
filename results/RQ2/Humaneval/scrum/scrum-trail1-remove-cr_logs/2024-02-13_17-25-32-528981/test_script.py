def choose_num(x, y):
    max_even = -1
    for num in range(x, y+1):
        if num % 2 == 0 and num > max_even:
            max_even = num
    return max_even
import unittest

class Test(unittest.TestCase):
    def test_choose_num(self):
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)

if __name__ == '__main__':
    unittest.main()