def is_woodall(x):
    if not isinstance(x, int) or x <= 0:
        return False  # input validation
    n = 1
    while True:
        result = n * (2 ** n - 1)
        if result == x:
            return True
        elif result > x:
            return False
        n += 1  # better variable naming and more comments to explain the logic
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_woodall(383), True)

if __name__ == '__main__':
    unittest.main()