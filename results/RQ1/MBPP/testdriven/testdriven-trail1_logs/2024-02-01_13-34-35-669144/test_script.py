def check_K(test_tup, K):
    if not isinstance(test_tup, tuple) or not isinstance(K, int):
        raise ValueError("Input validation failed: test_tup must be a tuple and K must be an integer")

    for item in test_tup:
        if item == K:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_K((10, 4, 5, 6, 8), 6), True)

if __name__ == '__main__':
    unittest.main()