def check_K(test_tup, K):
    if not isinstance(test_tup, tuple):
        raise ValueError("test_tup is not a tuple")
    if not isinstance(K, int):
        raise ValueError("K is not an integer")
    
    if test_tup is None or len(test_tup) == 0:
        return False
    
    return K in test_tup
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_K((10, 4, 5, 6, 8), 6), True)

if __name__ == '__main__':
    unittest.main()