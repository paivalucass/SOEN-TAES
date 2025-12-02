def max_val(listval):
    if not listval:
        return None
    
    max_value = None
    for item in listval:
        if isinstance(item, (int, float)):
            if max_value is None or item > max_value:
                max_value = item
    return max_value
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_val(['Python', 3, 2, 4, 5, 'version']), 5)

if __name__ == '__main__':
    unittest.main()