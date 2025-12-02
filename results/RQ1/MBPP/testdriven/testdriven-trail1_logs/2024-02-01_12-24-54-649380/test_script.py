def subtract_elements(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        return "Error: Unequal length of input tuples"

    for ele in test_tup1:
        if not isinstance(ele, (int, float)):
            return "Error: Non-numeric elements in input tuples"
    
    for ele in test_tup2:
        if not isinstance(ele, (int, float)):
            return "Error: Non-numeric elements in input tuples"

    result = tuple(x - y for x, y in zip(test_tup1, test_tup2))
    return result
import unittest

class Test(unittest.TestCase):
    def test_substract_elements(self):
        self.assertEqual(substract_elements((10, 4, 5), (2, 5, 18)), (8, -1, -13))

if __name__ == '__main__':
    unittest.main()