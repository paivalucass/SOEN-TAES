def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True

    start = 1
    end = n
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == n:
            return True
        if mid * mid < n:
            start = mid + 1
        else:
            end = mid - 1
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_perfect_square(10), False)

if __name__ == '__main__':
    unittest.main()