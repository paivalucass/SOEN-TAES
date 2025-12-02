def check_K(test_tup, K):
    if not test_tup:
        return False
    else:
        return K in test_tup

assert check_K((10, 4, 5, 6, 8), 6) == True
assert check_K((), 6) == False
assert check_K((1, 2, 3, 4, 5), 6) == False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_K((10, 4, 5, 6, 8), 6), True)

if __name__ == '__main__':
    unittest.main()