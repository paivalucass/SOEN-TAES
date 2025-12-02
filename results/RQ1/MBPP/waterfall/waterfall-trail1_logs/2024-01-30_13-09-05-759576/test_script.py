def min_val(listval):
    if not isinstance(listval, list):
        raise ValueError("Input should be a list")

    if not listval:
        raise ValueError("Input list is empty")

    numeric_values = [val for val in listval if isinstance(val, (int, float))]

    if not numeric_values:
        raise ValueError("No numeric values found in the input list")

    return min(numeric_values)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_val(['Python', 3, 2, 4, 5, 'version']), 2)

if __name__ == '__main__':
    unittest.main()