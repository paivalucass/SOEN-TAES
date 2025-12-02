def get_total_number_of_sequences(m, n):
    count = 0
    if n == 1:
        return m // 2
    for i in range(1, m // 2 + 1):
        count += get_total_number_of_sequences(i, n - 1)
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_total_number_of_sequences(10, 4), 4)

if __name__ == '__main__':
    unittest.main()