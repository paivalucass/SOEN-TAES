def last_digit(n):
    return int(str(n)[-1])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last_Digit(123), 3)

if __name__ == '__main__':
    unittest.main()