def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    start_point = max(interval1[0], interval2[0])
    end_point = min(interval1[1], interval2[1])
    
    if start_point > end_point:
        return "NO"

    length = end_point - start_point + 1
    if length <= 1:
        return "NO"

    if is_prime(length):
        return "YES"
    else:
        return "NO"
import unittest

class Test(unittest.TestCase):
    def test_intersection(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

if __name__ == '__main__':
    unittest.main()