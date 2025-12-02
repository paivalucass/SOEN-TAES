def is_perfect_square(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    else:
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == n:
                return True
            elif mid * mid < n:
                left = mid + 1
            else:
                right = mid - 1
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertFalse(is_perfect_square(10))

if __name__ == '__main__':
    unittest.main()