def newman_prime(n):
    if n < 0:
        return False
    elif n == 0 or n == 1:
        return False
    else:
        num = 2 ** (2 ** n) - 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return num

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(newman_prime(3), 7)

if __name__ == '__main__':
    unittest.main()