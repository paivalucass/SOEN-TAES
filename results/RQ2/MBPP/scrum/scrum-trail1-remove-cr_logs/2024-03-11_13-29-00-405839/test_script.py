def first_Digit(n) :
    if type(n) != int:
        return "Error: Input is not an integer"
    if n < 0:
        n = abs(n)
    while n >= 10:
        n = n // 10
    return n
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_Digit(123), 1)

if __name__ == '__main__':
    unittest.main()