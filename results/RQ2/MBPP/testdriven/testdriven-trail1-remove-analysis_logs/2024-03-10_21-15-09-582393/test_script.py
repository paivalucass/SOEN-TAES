def substract_elements(test_tup1, test_tup2):
    result = []
    if isinstance(test_tup1, tuple) and isinstance(test_tup2, tuple) and len(test_tup1) == len(test_tup2):
        for i in range(len(test_tup1)):
            result.append(test_tup1[i] - test_tup2[i])
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test_substract_elements(self):
        self.assertEqual(substract_elements((10, 4, 5), (2, 5, 18)), (8, -1, -13))

if __name__ == '__main__':
    unittest.main()