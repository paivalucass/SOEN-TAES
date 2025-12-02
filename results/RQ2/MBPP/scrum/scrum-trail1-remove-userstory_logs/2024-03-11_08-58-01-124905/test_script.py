def next_power_of_2(n):
    if not isinstance(n, int) or n < 0:
        return "Error"
    
    if n == 0:
        return 1
    
    power = 1
    while power < n:
        power <<= 1

    return power
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_power_of_2(0), 1)

if __name__ == '__main__':
    unittest.main()