def is_woodall(x):
    if not isinstance(x, int) or x <= 0:
        raise ValueError("Input must be a positive integer")

    for n in range(1, x):
        if x == n * 2**n - 1:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_woodall(383), True)

if __name__ == '__main__':
    unittest.main()