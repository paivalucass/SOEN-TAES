def is_polite(n):
    if not isinstance(n, int) or n < 1:
        return "Error message: Invalid input. Please enter a positive integer."
    polite_numbers = [1]
    current = 1
    while len(polite_numbers) < n:
        current += 1
        next_polite = current
        for num in polite_numbers:
            if num > current // 2:
                break
            next_polite -= num
        if next_polite > 0 and next_polite not in polite_numbers:
            polite_numbers.append(next_polite)
    return polite_numbers[n - 1] if n <= len(polite_numbers) else "Error message: Nth polite number is not available for current input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_polite(7), 11)

if __name__ == '__main__':
    unittest.main()