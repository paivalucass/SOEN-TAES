def highest_Power_of_2(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input"
    power = 1
    while power * 2 <= n:
        power *= 2
    return power
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(highest_Power_of_2(10), 8)

if __name__ == '__main__':
    unittest.main()