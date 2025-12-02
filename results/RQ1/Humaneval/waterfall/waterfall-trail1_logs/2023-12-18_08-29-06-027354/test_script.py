def tri(n):
    sequence = [0, 1, 1]
    if n < 3:
        return sequence[:n+1]
    for i in range(3, n+1):
        if i % 2 == 0:
            sequence.append(1 + i // 2)
        else:
            sequence.append(sequence[i-1] + sequence[i-2] + sequence[i-3])
    return sequence
import unittest

class TestTribonacci(unittest.TestCase):
    def test_tribonacci(self):
        self.assertEqual(tribonacci(3), [0, 1, 1, 2])
        self.assertEqual(tribonacci(4), [0, 1, 1, 2, 4])
        self.assertEqual(tribonacci(5), [0, 1, 1, 2, 4, 7])
        self.assertEqual(tribonacci(6), [0, 1, 1, 2, 4, 7, 13])

if __name__ == '__main__':
    unittest.main()