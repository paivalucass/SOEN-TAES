def check_none(test_tup):
    if not isinstance(test_tup, tuple):
        raise TypeError("Input should be a tuple")
    
    return any(x is None for x in test_tup)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_none((10, 4, 5, 6, None)), True)

if __name__ == '__main__':
    unittest.main()