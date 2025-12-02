def is_positive_integer(num):
    if isinstance(num, int) and num > 0:
        return True
    else:
        return False

def generate_collatz_sequence(n):
    collatz_sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        collatz_sequence.append(n)
    return collatz_sequence

def filter_odd_numbers(sequence):
    odd_numbers = [num for num in sequence if num % 2 != 0]
    return sorted(odd_numbers)

def get_odd_collatz(n):
    if not is_positive_integer(n):
        return "Invalid input"
    
    collatz_sequence = generate_collatz_sequence(n)
    return filter_odd_numbers(collatz_sequence)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

if __name__ == '__main__':
    unittest.main()