def maximize_elements(test_tup1, test_tup2):
    return tuple(map(lambda x, y: (max(x[0], y[0]), max(x[1], y[1])), test_tup1, test_tup2))
import unittest

class Test(unittest.TestCase):
    def test_maximize_elements(self):
        self.assertEqual(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))), ((6, 7), (4, 9), (2, 9), (7, 10)))

if __name__ == '__main__':
    unittest.main()