def check_K(test_tup, K):
    if test_tup is None or len(test_tup) == 0:
        raise ValueError("Input tuple is empty or null")
        
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