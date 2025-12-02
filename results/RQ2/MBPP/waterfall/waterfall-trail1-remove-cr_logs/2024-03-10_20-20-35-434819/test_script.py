def check_K(test_tup, K):
    if not isinstance(test_tup, tuple):
        raise Exception("Input is not a tuple")
    for element in test_tup:
        if element == K:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_K((10, 4, 5, 6, 8), 6), True)

if __name__ == '__main__':
    unittest.main()