def min_val(listval):
    if not isinstance(listval, list):
        raise TypeError("Input should be a list")
    if not any(isinstance(x, (int, float)) for x in listval):
        raise ValueError("List should contain numeric values")

    numeric_values = [x for x in listval if isinstance(x, (int, float))]
    if not numeric_values:
        raise ValueError("List does not contain any numeric values")

    return min(numeric_values)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_val(['Python', 3, 2, 4, 5, 'version']), 2)

if __name__ == '__main__':
    unittest.main()