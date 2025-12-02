def highest_power_of_2(n):
    if isinstance(n, int):
        if n > 0:
            return 1 << n.bit_length() - 1
        elif n == 0:
            return 0
        else:
            return -1 * (1 << (-n).bit_length())
    else:
        return 'Invalid input'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(highest_Power_of_2(10), 8)

if __name__ == '__main__':
    unittest.main()