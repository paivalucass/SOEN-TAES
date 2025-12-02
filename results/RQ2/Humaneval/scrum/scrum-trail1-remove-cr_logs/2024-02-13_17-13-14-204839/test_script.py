def get_odd_collatz(n):
    def collatz_sequence(n):
        sequence = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            sequence.append(n)
        return sequence

    def filter_odd_numbers(sequence):
        return sorted([num for num in sequence if num % 2 != 0])

    if not isinstance(n, int) or n <= 0:
        return "Invalid Input"

    sequence = collatz_sequence(n)
    odd_numbers = filter_odd_numbers(sequence)

    return odd_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

if __name__ == '__main__':
    unittest.main()