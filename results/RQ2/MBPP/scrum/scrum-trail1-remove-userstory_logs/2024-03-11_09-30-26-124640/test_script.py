def check_K(test_tup, K):
    if not isinstance(test_tup, tuple):
        raise TypeError("test_tup should be a tuple")
    if not isinstance(K, int):
        raise TypeError("K should be an integer")
    
    if K in test_tup:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_K((10, 4, 5, 6, 8), 6), True)

if __name__ == '__main__':
    unittest.main()