def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2

    if start1 <= end2 and start2 <= end1:
        intersection_start = max(start1, start2)
        intersection_end = min(end1, end2)
        intersection_length = intersection_end - intersection_start

        if intersection_length <= 1:
            return 'NO'

        for i in range(2, int(intersection_length ** 0.5) + 1):
            if intersection_length % i == 0:
                return 'NO'

        return 'YES'
    else:
        return 'NO'
import unittest

class Test(unittest.TestCase):
    def test_intersection(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

if __name__ == '__main__':
    unittest.main()