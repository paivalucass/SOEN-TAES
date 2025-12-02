def max_val(listval):
    max_value = None
    if not isinstance(listval, list):
        return "Error: Input is not a list"
    if not listval:
        return None
    
    for element in listval:
        if isinstance(element, (int, float)):
            if max_value is None or element > max_value:
                max_value = element
    
    return max_value
import unittest

class Test(unittest.TestCase):
    def test_max_val(self):
        self.assertEqual(max_val(['Python', 3, 2, 4, 5, 'version']), 5)

if __name__ == '__main__':
    unittest.main()