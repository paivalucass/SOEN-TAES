def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    length = max(0, (min(end1, end2) - max(start1, start2)) + 1)
    if length <= 1 or not is_prime(length):
        return 'NO'
    return 'YES'
import unittest

class Test(unittest.TestCase):
    def test_intersection(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

if __name__ == '__main__':
    unittest.main()