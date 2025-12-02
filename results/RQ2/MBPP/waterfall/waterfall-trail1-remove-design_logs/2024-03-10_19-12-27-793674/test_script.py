def max_val(listval):
    if not isinstance(listval, list):
        raise ValueError("Input must be a list")
    
    numeric_values = [x for x in listval if isinstance(x, (int, float)) or (isinstance(x, str) and x.isnumeric())]
    
    if not numeric_values:
        return None
    
    return max(numeric_values)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_val(['Python', 3, 2, 4, 5, 'version']), 5)

if __name__ == '__main__':
    unittest.main()