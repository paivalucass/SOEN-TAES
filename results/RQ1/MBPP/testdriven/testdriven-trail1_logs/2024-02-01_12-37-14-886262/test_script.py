def minimum(a, b):
    try:
        min_value = min(a, b)
        return min_value
    except Exception as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test_minimum(self):
        self.assertEqual(minimum(1, 2), 1)

if __name__ == '__main__':
    unittest.main()