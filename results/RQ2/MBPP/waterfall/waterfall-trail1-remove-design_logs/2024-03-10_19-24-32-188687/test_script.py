def check_none(test_tup):
    return any(item is None for item in test_tup)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_none((10, 4, 5, 6, None)), True)

if __name__ == '__main__':
    unittest.main()