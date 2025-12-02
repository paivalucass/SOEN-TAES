def maximize_elements(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Error: test_tup1 and test_tup2 have different lengths")
    if any(isinstance(i, tuple) for i in test_tup1) or any(isinstance(i, tuple) for i in test_tup2):
        raise TypeError("Error: test_tup1 and test_tup2 contain elements of different types")
    result = [tuple(max(test_tup1[i][j], test_tup2[i][j]) for j in range(len(test_tup1[i]))) for i in range(len(test_tup1))]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))), ((6, 7), (4, 9), (2, 9), (7, 10)))

if __name__ == '__main__':
    unittest.main()