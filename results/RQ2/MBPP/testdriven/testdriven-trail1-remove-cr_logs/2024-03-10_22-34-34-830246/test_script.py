def next_Perfect_Square(N):
    if N < 0:
        raise ValueError('Input must be a non-negative number')
    root = int(N ** 0.5) + 1
    return root * root
import unittest

class Test(unittest.TestCase):
    def test_next_Perfect_Square(self):
        self.assertEqual(next_Perfect_Square(35), 36)

if __name__ == '__main__':
    unittest.main()