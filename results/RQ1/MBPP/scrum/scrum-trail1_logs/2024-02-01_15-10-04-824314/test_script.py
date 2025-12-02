def substract_elements(test_tup1, test_tup2):
    result = tuple(map(lambda x, y: x - y, test_tup1, test_tup2))
    return result
import unittest

class Test(unittest.TestCase):
    def test_substract_elements(self):
        self.assertEqual(substract_elements((10, 4, 5), (2, 5, 18)), (8, -1, -13))

if __name__ == '__main__':
    unittest.main()