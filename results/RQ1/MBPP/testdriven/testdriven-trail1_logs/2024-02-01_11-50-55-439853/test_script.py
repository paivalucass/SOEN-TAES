def is_woodall(x):
    if x <= 1:
        return False
    n = 1
    result = 1
    while result <= x:
        if result == x:
            return True
        n += 1
        result = n * (2*n - 1)
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_woodall(383), True)

if __name__ == '__main__':
    unittest.main()