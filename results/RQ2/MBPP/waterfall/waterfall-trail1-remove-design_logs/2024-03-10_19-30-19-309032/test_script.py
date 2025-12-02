def sum_common_divisors(a, b):
    if a == 0 or b == 0:
        return 0
    common_divisors = []
    gcd = find_gcd(a, b)
    for i in range(1, gcd + 1):
        if gcd % i == 0:
            common_divisors.append(i)
    return sum(common_divisors)

def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

assert sum_common_divisors(10, 15) == 6
assert sum_common_divisors(100, 1000) == 233
assert sum_common_divisors(1, 1) == 1
assert sum_common_divisors(1000, 1000) == 233

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum(10, 15), 6)

if __name__ == '__main__':
    unittest.main()