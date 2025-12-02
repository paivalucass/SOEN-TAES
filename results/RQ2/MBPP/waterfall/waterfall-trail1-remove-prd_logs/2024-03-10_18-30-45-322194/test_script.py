def next_power_of_2(n):
    import math
    
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a positive integer")

    if n == 0:
        return 1
    if n & (n - 1) == 0:
        return n
    else:
        return 2 ** math.ceil(math.log2(n))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_power_of_2(0), 1)

if __name__ == '__main__':
    unittest.main()