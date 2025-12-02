def get_odd_collatz(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Invalid input: n must be a positive integer")

    odd_numbers_collatz = []

    while n != 1:
        if n % 2 == 1:
            odd_numbers_collatz.append(n)
        n = n * 3 + 1 if n % 2 else n // 2

    odd_numbers_collatz.append(1)  # Add 1 to the list as it is not included in the while loop
    odd_numbers_collatz.sort()

    return odd_numbers_collatz
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

if __name__ == '__main__':
    unittest.main()