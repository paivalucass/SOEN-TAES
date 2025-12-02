def count_divisors(n):
    if not isinstance(n, int):
        return "Invalid Input"
    if n <= 0:
        return False
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count % 2 == 0

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_divisors(10), True)

if __name__ == '__main__':
    unittest.main()