def is_undulating(n):
    if len(str(n)) < 3:
        return False
    digits = [int(d) for d in str(n)]
    for i in range(1, len(digits) - 1):
        if (digits[i] - digits[i-1]) * (digits[i] - digits[i+1]) <= 0:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_undulating(1212121), True)

if __name__ == '__main__':
    unittest.main()