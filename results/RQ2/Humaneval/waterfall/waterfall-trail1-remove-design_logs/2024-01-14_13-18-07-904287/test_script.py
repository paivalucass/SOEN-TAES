def get_odd_collatz(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    collatz_sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        collatz_sequence.append(n)
    
    return sorted([num for num in collatz_sequence if num % 2 != 0])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

if __name__ == '__main__':
    unittest.main()