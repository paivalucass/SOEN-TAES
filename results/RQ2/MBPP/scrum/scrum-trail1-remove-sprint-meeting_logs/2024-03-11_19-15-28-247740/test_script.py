def check_K(test_tup, K):
    if not isinstance(test_tup, tuple):
        raise ValueError("test_tup must be a tuple")
    if not isinstance(K, (int, float)):
        raise ValueError("K must be a valid value")

    return K in test_tup

# Test cases
assert check_K((10, 4, 5, 6, 8), 6) == True
assert check_K((), 6) == False
assert check_K((10, 4, 5, 6, 8), 11) == False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_K((10, 4, 5, 6, 8), 6), True)

if __name__ == '__main__':
    unittest.main()