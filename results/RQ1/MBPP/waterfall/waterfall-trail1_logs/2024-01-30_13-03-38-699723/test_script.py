def highest_Power_of_2(n):
    if not isinstance(n, int):
        return "Invalid input"
    if n <= 0:
        return 0
    power = 0
    while (1 << power) <= n:
        power += 1
    return 1 << (power - 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(highest_Power_of_2(10), 8)

if __name__ == '__main__':
    unittest.main()