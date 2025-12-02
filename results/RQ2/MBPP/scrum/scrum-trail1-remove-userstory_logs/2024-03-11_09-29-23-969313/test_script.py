def sum_odd(l, r):
    total = 0
    if not isinstance(l, int) or not isinstance(r, int):
        return "Invalid input: l and r must be integers"

    if l > r:
        return "Invalid input: l must be less than or equal to r"

    for num in range(l, r+1):
        if num % 2 != 0:
            total += num

    return total
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_odd(2, 5), 8)

if __name__ == '__main__':
    unittest.main()