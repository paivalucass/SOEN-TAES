def max_sub_array_sum(a, size):
    if size <= 0 or len(a) < size:
        return 0

    max_ending_here = max_so_far = a[0]

    for i in range(1, size):
        max_ending_here = max(a[i], max_ending_here + a[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8), 7)

if __name__ == '__main__':
    unittest.main()