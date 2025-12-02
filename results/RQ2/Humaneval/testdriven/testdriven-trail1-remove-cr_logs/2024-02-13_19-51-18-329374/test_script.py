def get_odd_collatz(n):
    result = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        if n % 2 != 0:
            result.append(n)
    return sorted(result)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_odd_collatz(5), [1, 5])

if __name__ == '__main__':
    unittest.main()