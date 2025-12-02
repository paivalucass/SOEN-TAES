def divisor(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i < n:
                count += 2
            else:
                count += 1
        i += 1
    return count

import unittest

class Test(unittest.TestCase):
    def test_divisor(self):
        self.assertEqual(divisor(15), 4)

if __name__ == '__main__':
    unittest.main()