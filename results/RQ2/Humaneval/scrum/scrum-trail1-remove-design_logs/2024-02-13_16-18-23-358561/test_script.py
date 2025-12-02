def count_nums(arr):
    count = 0
    for num in arr:
        if sum(int(digit) for digit in str(num).lstrip('-')) > 0:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_nums([]), 0)
        self.assertEqual(count_nums([-1, 11, -11]), 1)
        self.assertEqual(count_nums([1, 1, 2]), 3)

if __name__ == '__main__':
    unittest.main()