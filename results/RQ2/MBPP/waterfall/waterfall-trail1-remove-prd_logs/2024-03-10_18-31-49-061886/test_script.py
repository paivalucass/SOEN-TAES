def get_total_number_of_sequences(m, n):
    sequences = [[0] * (m + 1) for _ in range(n + 1)]
    for j in range(1, m + 1):
        sequences[1][j] = 1
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            for k in range(j * 2, m + 1):
                sequences[i][k] += sequences[i - 1][j]

    total_sequences = sum(sequences[n])
    return total_sequences
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_total_number_of_sequences(10, 4), 4)

if __name__ == '__main__':
    unittest.main()