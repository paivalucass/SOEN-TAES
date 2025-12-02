def is_woodall(x):
    result = 1
    n = 1
    while result < x:
        result = n * (2 ** n - 1)
        if result == x:
            return True
        n += 1
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_woodall(383), True)

if __name__ == '__main__':
    unittest.main()