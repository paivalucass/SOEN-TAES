def newman_prime(n):
    if n <= 0:
        raise ValueError("Input value must be greater than 0")

    nth_newman_prime = 0
    count = 0
    num = 1

    while(count < n):
        num += 1
        if is_newman_prime(num):
            count += 1
            nth_newman_prime = num

    return nth_newman_prime

def is_newman_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(newman_prime(3), 7)

if __name__ == '__main__':
    unittest.main()