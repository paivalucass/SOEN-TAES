def is_perfect_square(n):
    if type(n) != int:
        return "Invalid Input"
    if n < 0:
        return False
    left = 0
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
        self.assertEqual(is_perfect_square(10), False)

if __name__ == '__main__':
    unittest.main()