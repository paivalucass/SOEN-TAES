def is_polite(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    polite_numbers = [1]
    i, j = 0, 0

    while len(polite_numbers) < n:
        next_num = min(2*polite_numbers[i], 3*polite_numbers[j])
        polite_numbers.append(next_num)

        if next_num == 2*polite_numbers[i]:
            i += 1
        if next_num == 3*polite_numbers[j]:
            j += 1

    return polite_numbers[n-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_polite(7), 11)

if __name__ == '__main__':
    unittest.main()