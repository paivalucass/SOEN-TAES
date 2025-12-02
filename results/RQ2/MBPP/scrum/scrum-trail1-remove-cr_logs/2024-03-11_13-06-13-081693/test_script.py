def max_val(listval):
    if not listval:
        return "Error Handling for Empty List"

    # Filter out non-numeric values and use max() function to find the maximum value
    numeric_values = [x for x in listval if isinstance(x, (int, float))]
    if not numeric_values:
        return "Error Handling for List with Only Negative Numbers"

    return max(numeric_values)  # Return the maximum value
import unittest

class Test(unittest.TestCase):
    def test_max_val(self):
        self.assertEqual(max_val(['Python', 3, 2, 4, 5, 'version']), 5)

if __name__ == '__main__':
    unittest.main()