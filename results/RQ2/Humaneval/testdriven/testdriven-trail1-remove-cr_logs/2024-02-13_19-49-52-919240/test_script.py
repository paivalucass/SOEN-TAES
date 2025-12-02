def count_nums(arr):
    total_count = 0
    for num in arr:
        if sum(int(d) for d in str(abs(num))) > 0:
            total_count += 1
    return total_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test([]), 0)
        self.assertEqual(function_under_test([-1, 11, -11]), 1)
        self.assertEqual(function_under_test([1, 1, 2]), 3)

if __name__ == '__main__':
    unittest.main()