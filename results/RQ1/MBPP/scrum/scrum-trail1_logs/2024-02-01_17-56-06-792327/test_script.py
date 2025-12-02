def count_X(tup, x):
    count = 0
    if not isinstance(tup, tuple):
        raise ValueError("Input parameter 'tup' must be a tuple")
    if x not in tup:
        return count
    for element in tup:
        if element == x:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4), 0)

if __name__ == '__main__':
    unittest.main()