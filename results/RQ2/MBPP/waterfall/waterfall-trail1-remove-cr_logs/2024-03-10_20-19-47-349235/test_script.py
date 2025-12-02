def sum_odd(l, r):
    if not isinstance(l, int) or not isinstance(r, int) or l < 0 or r < 0:
        return "Invalid input, please enter positive integers for the range l and r"

    if l > r:
        return "Invalid input, range start should be less than or equal to range end"

    result = 0
    for i in range(l, r+1):
        if i % 2 != 0:
            result += i

    return result
import unittest

class Test(unittest.TestCase):
    def test_sum_odd(self):
        self.assertEqual(sum_odd(2, 5), 8)

if __name__ == '__main__':
    unittest.main()