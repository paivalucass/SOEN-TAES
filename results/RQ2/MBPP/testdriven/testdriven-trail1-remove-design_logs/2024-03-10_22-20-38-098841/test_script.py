def check_K(test_tup, K):
    if not isinstance(test_tup, tuple):
        raise TypeError("Input is not a tuple")
    if not isinstance(K, (int, float, str)):
        raise TypeError("Invalid type for comparison")
    
    return K in test_tup
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_K((10, 4, 5, 6, 8), 6), True)

if __name__ == '__main__':
    unittest.main()