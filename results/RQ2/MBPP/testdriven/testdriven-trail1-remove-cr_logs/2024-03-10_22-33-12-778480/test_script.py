def next_power_of_2(n):
    result = 1
    while result < n:
        result *= 2
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_power_of_2(0), 1)

if __name__ == '__main__':
    unittest.main()