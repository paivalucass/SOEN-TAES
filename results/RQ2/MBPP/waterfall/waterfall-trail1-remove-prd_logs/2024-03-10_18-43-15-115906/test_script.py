def is_Even(n):
    return n % 2 == 0

assert is_Even(1) == False
assert is_Even(2) == True
assert is_Even(0) == True
assert is_Even(-2) == True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Even(1), False)

if __name__ == '__main__':
    unittest.main()