def get_total_number_of_sequences(m, n):
    if n == 0:
        return 1
    count = 0
    for i in range(1, m // 2 + 1):
        if m - i >= 2:
            count += get_total_number_of_sequences(m - i, n - 1)
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_total_number_of_sequences(10, 4), 4)

if __name__ == '__main__':
    unittest.main()