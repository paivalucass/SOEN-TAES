def count_nums(arr):
    if not arr:
        return 0
    count = 0
    for num in arr:
        num_str = str(abs(num))
        if sum(int(digit) for digit in num_str) > 0:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_count_nums(self):
        self.assertEqual(count_nums([]), 0)
        self.assertEqual(count_nums([-1, 11, -11]), 1)
        self.assertEqual(count_nums([1, 1, 2]), 3)

if __name__ == '__main__':
    unittest.main()