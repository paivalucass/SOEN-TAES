def max_val(listval):
    numeric_values = [x for x in listval if isinstance(x, (int, float))]
    if not numeric_values:
        return "List contains non-numeric values"
    return max(numeric_values)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_val(['Python', 3, 2, 4, 5, 'version']), 5)

if __name__ == '__main__':
    unittest.main()