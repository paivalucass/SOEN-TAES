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
        return [num for num in sequence if num % 2 != 0]

    def sort_numbers_increasing(numbers):
        return sorted(numbers)

    return sort_numbers_increasing(filter_odd_numbers(collatz_sequence(n)))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

if __name__ == '__main__':
    unittest.main()