def max_sub_array_sum(a, size):
    if not a or size <= 0:
        return 0

    max_sum_contiguous_sublist = a[0]
    current_sum = a[0]

    for i in range(1, size):
        current_sum = max(a[i], current_sum + a[i])
        max_sum_contiguous_sublist = max(max_sum_contiguous_sublist, current_sum)

    return max_sum_contiguous_sublist
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8), 7)

if __name__ == '__main__':
    unittest.main()