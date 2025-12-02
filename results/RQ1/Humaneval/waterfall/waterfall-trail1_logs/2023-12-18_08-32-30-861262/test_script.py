def get_max_triples(n):
    if n <= 0:
        return 0

    def generate_sequence(n):
        sequence = [0] * n
        for i in range(0, n):
            sequence[i] = i * i - i + 1
        return sequence

    def count_valid_triples(sequence):
        count = 0
        for i in range(0, len(sequence) - 2):
            for j in range(i + 1, len(sequence) - 1):
                for k in range(j + 1, len(sequence)):
                    if (sequence[i] + sequence[j] + sequence[k]) % 3 == 0:
                        count += 1
        return count

    return count_valid_triples(generate_sequence(n))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_max_triples(5), 1)

if __name__ == '__main__':
    unittest.main()