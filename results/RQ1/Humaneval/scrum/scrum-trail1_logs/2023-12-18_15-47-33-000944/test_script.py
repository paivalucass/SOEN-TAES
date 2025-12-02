def intersection(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    start = max(start1, start2)
    end = min(end1, end2)
    if start > end:
        return 'NO'
    length = end - start + 1
    if length <= 1:
        return 'NO'
    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return 'NO'
    return 'YES'
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