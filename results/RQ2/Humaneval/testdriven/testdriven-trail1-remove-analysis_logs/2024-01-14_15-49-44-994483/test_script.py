def fibfib(n: int):
    """Function to efficiently compute the n-th element of the fibfib number sequence."""
    fib_sequence = [0, 0, 1]  # Initialize with the first three elements of the sequence

    if n < 0 or not isinstance(n, int):
        return "Invalid input"  # Error handling for invalid input

    for i in range(3, n+1):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2] + fib_sequence[i-3]
        fib_sequence.append(next_fib)

    return fib_sequence[n]  # Return the n-th element of the fibfib sequence
import unittest

class Test(unittest.TestCase):
    def test_fibfib(self):
        self.assertEqual(fibfib(1), 0)
        self.assertEqual(fibfib(5), 4)
        self.assertEqual(fibfib(8), 24)

if __name__ == '__main__':
    unittest.main()