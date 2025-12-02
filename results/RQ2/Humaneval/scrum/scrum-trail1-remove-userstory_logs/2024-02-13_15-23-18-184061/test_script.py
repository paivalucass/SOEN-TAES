def get_odd_collatz(n):
    odd_numbers = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            odd_numbers.append(n)
            n = 3 * n + 1
    odd_numbers.append(1)
    return sorted(odd_numbers)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

if __name__ == '__main__':
    unittest.main()