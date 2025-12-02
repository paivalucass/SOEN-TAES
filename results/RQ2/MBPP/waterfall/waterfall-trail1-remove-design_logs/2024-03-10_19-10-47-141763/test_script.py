def division_elements(test_tup1, test_tup2):
    result = []
    for x, y in zip(test_tup1, test_tup2):
        if y != 0:
            result.append(x // y)
        else:
            result.append(None)  # Handle division by zero
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test_division_elements(self):
        self.assertEqual(division_elements((10, 4, 6, 9),(5, 2, 3, 3)), (2, 2, 2, 3))

if __name__ == '__main__':
    unittest.main()