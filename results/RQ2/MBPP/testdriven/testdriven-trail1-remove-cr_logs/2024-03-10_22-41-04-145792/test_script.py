def and_tuples(test_tup1, test_tup2):
    return tuple(x & y for x, y in zip(test_tup1, test_tup2))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(and_tuples((10, 4, 6, 9), (5, 2, 3, 3)), (0, 0, 2, 1))

if __name__ == '__main__':
    unittest.main()