def max_val(listval):
    max_value = None
    for val in listval:
        if isinstance(val, int) or isinstance(val, float):
            if max_value is None or val > max_value:
                max_value = val
    return max_value
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_val(['Python', 3, 2, 4, 5, 'version']), 5)

if __name__ == '__main__':
    unittest.main()