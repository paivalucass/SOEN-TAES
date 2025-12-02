def choose_num(x, y):
    if x % 2 != 0:
        x += 1

    largest_even = None
    while x <= y:
        if x % 2 == 0:
            largest_even = x
        x += 2

    if largest_even:
        return largest_even
    else:
        return -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)

if __name__ == '__main__':
    unittest.main()