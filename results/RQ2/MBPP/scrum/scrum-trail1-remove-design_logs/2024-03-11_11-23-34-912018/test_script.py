def highest_Power_of_2(n):
    power = 0
    while 2 ** power <= n:
        power += 1
    return 2 ** (power - 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(highest_Power_of_2(10), 8)

if __name__ == '__main__':
    unittest.main()