def max_val(listval):
    if len(listval) == 0:
        raise ValueError("Error: Empty list")

    valid_types = (int, float, str)
    for item in listval:
        if not isinstance(item, valid_types):
            raise TypeError("Invalid data type in the input list")

    numeric_values = [item for item in listval if isinstance(item, (int, float))]
    if len(numeric_values) == 0:
        raise ValueError("Error: No numeric values in the list")

    max_value = max(numeric_values)
    return max_value
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_val([3, 2, 4, 5]), 5)

if __name__ == '__main__':
    unittest.main()