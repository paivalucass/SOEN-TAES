def highest_power_of_2(n):
    result = 1
    while result * 2 <= n:
        result = result * 2
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(highest_Power_of_2(10), 8)

if __name__ == '__main__':
    unittest.main()