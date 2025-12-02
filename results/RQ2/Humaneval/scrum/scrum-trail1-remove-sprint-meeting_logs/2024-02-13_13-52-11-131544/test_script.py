def pairs_sum_to_zero(lst):
    if not all(isinstance(x, int) for x in lst):
        raise ValueError("Input list should contain only integers")

    seen = set()
    for num in lst:
        if -num in seen:
            return True
        seen.add(num)
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pairs_sum_to_zero([1, 3, 5, 0]), False)
        self.assertEqual(pairs_sum_to_zero([1, 3, -2, 1]), False)
        self.assertEqual(pairs_sum_to_zero([1, 2, 3, 7]), False)
        self.assertEqual(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]), True)
        self.assertEqual(pairs_sum_to_zero([1]), False)

if __name__ == '__main__':
    unittest.main()