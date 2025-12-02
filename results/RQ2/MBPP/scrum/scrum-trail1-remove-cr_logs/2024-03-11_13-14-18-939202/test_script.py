def min_val(listval):
    try:
        numeric_values = [val for val in listval if isinstance(val, (int, float))]
        if not numeric_values:
            raise ValueError("No numerical value found in the list")
        return min(numeric_values)
    except Exception as e:
        print(f"Error occurred: {e}")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_val(['Python', 3, 2, 4, 5, 'version']), 2)

if __name__ == '__main__':
    unittest.main()