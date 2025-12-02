def highest_Power_of_2(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    power = 0
    while n >= 2:
        n //= 2
        power += 1

    return 2 ** power
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(highest_Power_of_2(10), 8)

if __name__ == '__main__':
    unittest.main()