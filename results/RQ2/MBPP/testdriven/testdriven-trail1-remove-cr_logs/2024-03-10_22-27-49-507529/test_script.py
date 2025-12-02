def is_woodall(x):
    if x <= 0:
        return False
    else:
        result = x * 2**x - 1
        return result == x * 2**x - 1

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_woodall(383), True)

if __name__ == '__main__':
    unittest.main()