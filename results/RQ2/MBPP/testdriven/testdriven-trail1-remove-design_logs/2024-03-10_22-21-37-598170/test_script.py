def get_total_number_of_sequences(m, n):
    if m <= 0 or n <= 0 or not isinstance(m, int) or not isinstance(n, int):
        return 0
    if m < n:
        return 0
    if m == 0 and n == 0:
        return 1
    if n == 1:
        return m
    if n == 2:
        return m // 2
    count = 0
    for i in range(1, m // 2 + 1):
        count += get_total_number_of_sequences(m - i * 2, n - 1)
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_total_number_of_sequences(10, 4), 4)

if __name__ == '__main__':
    unittest.main()