def get_total_number_of_sequences(m, n):
    count = 0
    for i in range(1, m//2 + 1):
        count += get_sequences_count(i, m, n-1)
    return count


def get_sequences_count(prev, m, n):
    if n == 0:
        return 1
    count = 0
    for i in range(prev*2, m+1):
        count += get_sequences_count(i, m, n-1)
    return count


assert get_total_number_of_sequences(10, 4) == 4
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_total_number_of_sequences(10, 4), 4)

if __name__ == '__main__':
    unittest.main()