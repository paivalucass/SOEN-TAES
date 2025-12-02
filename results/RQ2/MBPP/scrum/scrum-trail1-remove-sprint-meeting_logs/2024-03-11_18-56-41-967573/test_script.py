def armstrong_number(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer")

    temp = number
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    return sum == number

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(armstrong_number(153), True)

if __name__ == '__main__':
    unittest.main()