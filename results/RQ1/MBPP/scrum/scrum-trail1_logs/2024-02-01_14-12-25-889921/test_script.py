def is_woodall(x):
    n = 1
    while True:
        result = n * (2 ** n - 1)
        if result == x:
            return True
        elif result > x:
            return False
        n += 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_woodall(383), True)

if __name__ == '__main__':
    unittest.main()