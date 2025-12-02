def division_elements(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        return "Error: Unequal length input tuples"
    
    if len(test_tup1) == 0 or len(test_tup2) == 0:
        return "Error: Empty input tuples"
    
    result_tup = []
    for i in range(len(test_tup1)):
        try:
            result = test_tup1[i] / test_tup2[i]
            result_tup.append(result)
        except ZeroDivisionError:
            return "Error: Division by zero"
    
    return tuple(result_tup)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(division_elements((10, 4, 6, 9), (5, 2, 3, 3)), (2, 2, 2, 3))

if __name__ == '__main__':
    unittest.main()