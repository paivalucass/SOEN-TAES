def sequence(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Error: Input must be a non-negative integer")

    if n == 0:
        return "Error: Input must be a non-negative integer"
    if n == 1:
        return 1
    if n == 2:
        return 1

    fibonacci_sequence = [0, 1, 1]

    for i in range(3, n + 1):
        fibonacci_sequence.append(fibonacci_sequence[fibonacci_sequence[i - 1]] + fibonacci_sequence[i - fibonacci_sequence[i - 1]])

    if n <= 1000000:
        return fibonacci_sequence[n]
    else:
        return "Result exceeds maximum value"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequence(10), 6)

if __name__ == '__main__':
    unittest.main()