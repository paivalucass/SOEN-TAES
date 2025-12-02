def last_Digit(n) :
    try:
        return abs(int(n)) % 10
    except ValueError:
        return "Input is not an integer"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last_Digit(123), 3)

if __name__ == '__main__':
    unittest.main()