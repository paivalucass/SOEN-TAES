def is_woodall(x): 
    result = 1
    n = 1
    while result < x:
        n += 1
        result = n * (n * 2 - 1)
    return result == x

import unittest

class Test(unittest.TestCase):
    def test_woodall(self):
        self.assertEqual(is_woodall(383), True)

if __name__ == '__main__':
    unittest.main()