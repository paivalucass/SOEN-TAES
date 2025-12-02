def division_elements(test_tup1, test_tup2):
    if not isinstance(test_tup1, tuple) or not isinstance(test_tup2, tuple):
        raise TypeError("Error - Input should be tuples")

    if len(test_tup1) != len(test_tup2):
        raise ValueError("Error - Tuples have different lengths")

    result = ()
    for i in range(len(test_tup1)):
        if not (isinstance(test_tup1[i], (int, float)) and isinstance(test_tup2[i], (int, float))):
            raise TypeError("Error - Tuples contain non-numeric values")

        try:
            division_result = test_tup1[i] / test_tup2[i]
            result += (division_result,)
        except ZeroDivisionError:
            result += ("Error - Division by zero",)

    if len(result) == 0:
        raise ValueError("Error - Empty tuples")

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(division_elements((10, 4, 6, 9),(5, 2, 3, 3)), (2, 2, 2, 3))

if __name__ == '__main__':
    unittest.main()