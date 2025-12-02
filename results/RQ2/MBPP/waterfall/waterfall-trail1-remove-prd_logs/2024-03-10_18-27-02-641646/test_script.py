def is_Diff(n):
    if not isinstance(n, int) or n <= 0:
        return False

    n_str = str(n)
    even_sum = sum(int(n_str[i]) for i in range(0, len(n_str), 2))
    odd_sum = sum(int(n_str[i]) for i in range(1, len(n_str), 2))

    diff = abs(even_sum - odd_sum)
    
    return diff % 11 == 0

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Diff(12345), False)

if __name__ == '__main__':
    unittest.main()