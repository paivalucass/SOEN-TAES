def validate(n):
    digits = [int(i) for i in str(n)]
    for digit in digits:
        count = digits.count(digit)
        if count > digit:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(validate(1234), True)

if __name__ == '__main__':
    unittest.main()