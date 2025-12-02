def max_val(listval):
    max_num = None
    for val in listval:
        if isinstance(val, (int, float)):
            if max_num is None or val > max_num:
                max_num = val
    if max_num is None:
        return 'Error: List contains non-numeric values'
    return max_num
import unittest

class Test(unittest.TestCase):
    def test_max_val(self):
        self.assertEqual(max_val(['Python', 3, 2, 4, 5, 'version']), 5)

if __name__ == '__main__':
    unittest.main()