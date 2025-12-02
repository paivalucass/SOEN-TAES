def intersection(interval1, interval2):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    if start > end:
        return "NO"  # No intersection
    length = end - start + 1

    if is_prime(abs(length)):
        return "YES"
    else:
        return "NO"
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(function_under_test((1, 2), (2, 3)), "NO")
    
    def test2(self):
        self.assertEqual(function_under_test((-1, 1), (0, 4)), "NO")
    
    def test3(self):
        self.assertEqual(function_under_test((-3, -1), (-5, 5)), "YES")

if __name__ == '__main__':
    unittest.main()