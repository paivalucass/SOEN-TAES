def count_X(tup, x):
    count = 0
    for element in tup:
        if element == x:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_count_X(self):
        self.assertEqual(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 10), 2)
        self.assertEqual(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 8), 4)
        self.assertEqual(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4), 0)

if __name__ == '__main__':
    unittest.main()