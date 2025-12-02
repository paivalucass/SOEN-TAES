def get_total_number_of_sequences(m, n):
    if not isinstance(m, int) or not isinstance(n, int) or m <= 0 or n <= 0:
        raise ValueError("m and n must be positive integers")

    count = 0
    for i in range(1, m+1):
        if i >= 2:
            count += get_sequences_helper(m, n-1, i)
    return count

def get_sequences_helper(m, n, prev):
    if n == 0:
        return 1
    count = 0
    for i in range(prev*2, m+1):
        count += get_sequences_helper(m, n-1, i)
    return count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_total_number_of_sequences(10, 4), 4)

if __name__ == '__main__':
    unittest.main()