def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_intersection_length(interval1, interval2):
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    return max(0, end - start + 1)

def intersection(interval1, interval2):
    if not (interval1[0] <= interval1[1] and interval2[0] <= interval2[1]):
        return "Invalid input intervals"
    length = calculate_intersection_length(interval1, interval2)
    if length < 2 or not is_prime(length):
        return "NO"
    return "YES"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

if __name__ == '__main__':
    unittest.main()