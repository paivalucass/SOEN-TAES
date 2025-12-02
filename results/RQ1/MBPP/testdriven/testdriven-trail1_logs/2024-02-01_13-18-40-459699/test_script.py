def geometric_sum(n):
    '''This function calculates the geometric sum of n-1.'''
    if not isinstance(n, int):
        raise ValueError("Input n should be an integer")
    elif n < 0:
        raise ValueError("Input n should be a non-negative integer")
    elif n == 0:
        return 1.0
    elif n == 1:
        return 2.0
    else:
        return 1 + 1 / geometric_sum(n - 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(geometric_sum(7), 1.9921875)

if __name__ == '__main__':
    unittest.main()