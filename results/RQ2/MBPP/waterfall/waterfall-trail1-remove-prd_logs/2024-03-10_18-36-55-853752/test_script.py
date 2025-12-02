def min_val(listval):
    if len(listval) == 0:
        raise ValueError("Input list must not be empty")

    min_value = None

    for val in listval:
        if isinstance(val, int) or isinstance(val, float):
            if min_value is None or val < min_value:
                min_value = val

    if min_value is None:
        raise ValueError("No numeric value found in the list")

    return min_value
import unittest

class Test(unittest.TestCase):
    def test_min_val(self):
        self.assertEqual(min_val(['Python', 3, 2, 4, 5, 'version']), 2)

if __name__ == '__main__':
    unittest.main()