def division_elements(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Length of input tuples are not equal")
    result = []
    for i in range(len(test_tup1)):
        if not isinstance(test_tup1[i], (int, float)) or not isinstance(test_tup2[i], (int, float)):
            raise TypeError("Non-integer inputs are not allowed")
        if test_tup2[i] == 0:
            raise ZeroDivisionError("Division by zero error")
        result.append(test_tup1[i] / test_tup2[i])
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(division_elements((10, 4, 6, 9), (5, 2, 3, 3)), (2, 2, 2, 3))

if __name__ == '__main__':
    unittest.main()