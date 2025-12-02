

def is_equal_to_sum_even(n):
    if not isinstance(n, int) or n <= 0:
        return False
    count = 0
    for i in range(1, n):
        if i % 2 == 0 and (n - i) % 2 == 0:
            count += 1
            if count == 4:
                return True
    return False

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_equal_to_sum_even(4), False)
        self.assertEqual(is_equal_to_sum_even(6), False)
        self.assertEqual(is_equal_to_sum_even(8), True)

if __name__ == '__main__':
    unittest.main()