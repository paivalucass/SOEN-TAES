def tri(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    if n == 0:
        return [0]

    tribonacci_sequence = [0, 1, 1]

    for i in range(3, n + 1):
        if i % 2 == 0:
            next_tribonacci = 1 + i // 2
        else:
            next_tribonacci = tribonacci_sequence[i - 1] + tribonacci_sequence[i - 2] + tribonacci_sequence[i - 3]
        tribonacci_sequence.append(next_tribonacci)

    return tribonacci_sequence
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tri(3), [0, 1, 1, 3])

if __name__ == '__main__':
    unittest.main()