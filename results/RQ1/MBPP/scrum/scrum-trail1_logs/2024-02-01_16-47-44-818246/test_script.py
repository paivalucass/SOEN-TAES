def is_polite(n):
    if not isinstance(n, int) or n <= 0:
        return "Error: Invalid input, n should be a positive integer."

    polite_numbers = [1]
    current_number = 2
    while len(polite_numbers) < n:
        if sum([i for i in range(1, current_number) if current_number % i == 0]) == current_number:
            polite_numbers.append(current_number)
        current_number += 1

    return polite_numbers[-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_polite(7), 11)

if __name__ == '__main__':
    unittest.main()