def validate(n):
    if not isinstance(n, int) or n <= 0:
        return False
    
    digit_count = [0] * 10
    while n > 0:
        digit = n % 10
        digit_count[digit] += 1
        if digit_count[digit] > digit:
            return False
        n = n // 10
    
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(validate(1234), True)

if __name__ == '__main__':
    unittest.main()