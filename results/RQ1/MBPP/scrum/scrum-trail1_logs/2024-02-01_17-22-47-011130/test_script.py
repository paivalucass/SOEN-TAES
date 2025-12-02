def max_val(listval):
    numeric_values = [val for val in listval if isinstance(val, (int, float))]
    if not numeric_values:
        return "Error message"
    return max(numeric_values)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_val(['Python', 3, 2, 4, 5, 'version']), 5)

if __name__ == '__main__':
    unittest.main()