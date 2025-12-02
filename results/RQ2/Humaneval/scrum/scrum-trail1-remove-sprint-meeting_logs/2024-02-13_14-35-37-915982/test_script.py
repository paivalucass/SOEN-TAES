def intersection(interval1, interval2):
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    length = end - start + 1
    if length <= 1:
        return 'NO'
    for i in range(2, int(length**0.5) + 1):
        if length % i == 0:
            return 'NO'
    return 'YES'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test((1, 2), (2, 3)), "NO")
        self.assertEqual(function_under_test((-1, 1), (0, 4)), "NO")
        self.assertEqual(function_under_test((-3, -1), (-5, 5)), "YES")

if __name__ == '__main__':
    unittest.main()