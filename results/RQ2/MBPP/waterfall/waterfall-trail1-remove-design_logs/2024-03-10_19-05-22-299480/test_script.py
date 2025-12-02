def sequence(n):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        sequence = [0] * (n + 1)
        sequence[1] = 1
        sequence[2] = 1
        for i in range(3, n + 1):
            sequence[i] = sequence[sequence[i - 1]] + sequence[i - sequence[i - 1]]
        return sequence[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequence(10), 6)

if __name__ == '__main__':
    unittest.main()