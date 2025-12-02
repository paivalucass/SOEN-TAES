def highest_Power_of_2(n):
    if not isinstance(n, int) or n <= 0:
        return "Input should be a positive integer"

    power_of_2 = 1
    while (power_of_2 * 2) <= n:
        power_of_2 = power_of_2 << 1
    return power_of_2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(highest_Power_of_2(10), 8)

if __name__ == '__main__':
    unittest.main()