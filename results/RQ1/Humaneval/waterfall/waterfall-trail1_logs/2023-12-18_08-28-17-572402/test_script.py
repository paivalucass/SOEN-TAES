def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2

    if start1 > end1 or start2 > end2:
        return "NO"
    if end1 < start2 or end2 < start1:
        return "NO"

    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)

    if intersection_start > intersection_end:
        return "NO"

    length = intersection_end - intersection_start + 1

    if is_prime(length):
        return "YES"
    else:
        return "NO"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

if __name__ == '__main__':
    unittest.main()