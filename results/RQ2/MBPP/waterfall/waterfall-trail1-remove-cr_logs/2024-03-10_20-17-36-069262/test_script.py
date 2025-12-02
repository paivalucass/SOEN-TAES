def is_polite(n):
    if not isinstance(n, int):
        return "Invalid input, please enter a valid integer value for n"
    if n <= 0:
        return "Please enter a positive integer value for n"
    if n > 1000:
        return "Polite number calculation exceeds limit, please enter a smaller integer value for n"

    # Memoization to optimize performance
    polite_numbers = [1, 2]
    if n <= 2:
        return polite_numbers[n-1]
    for i in range(2, n):
        next_polite = polite_numbers[-1] + polite_numbers[-2] + 1
        polite_numbers.append(next_polite)

    return polite_numbers[-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_polite(7), 11)

if __name__ == '__main__':
    unittest.main()