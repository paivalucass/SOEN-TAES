def division_elements(test_tup1, test_tup2):
    if not all(isinstance(x, (int, float)) for x in test_tup1) or not all(isinstance(x, (int, float)) for x in test_tup2):
        raise ValueError("Input tuples should contain only numeric values")

    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples should have the same length")

    try:
        result = tuple(x / y for x, y in zip(test_tup1, test_tup2))
        return result
    except ZeroDivisionError:
        raise ValueError("Division by zero is not allowed")
import unittest

class Test(unittest.TestCase):
    def test_division_elements(self):
        self.assertEqual(division_elements((10, 4, 6, 9),(5, 2, 3, 3)), (2, 2, 2, 3))

if __name__ == '__main__':
    unittest.main()