def first_Digit(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input number should be a positive integer")
    
    return int(str(n)[0])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_Digit(123), 1)

if __name__ == '__main__':
    unittest.main()