def get_odd_collatz(n):
    odd_collatz = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n % 2 != 0:
            odd_collatz.append(n)
    return sorted(odd_collatz)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

if __name__ == '__main__':
    unittest.main()