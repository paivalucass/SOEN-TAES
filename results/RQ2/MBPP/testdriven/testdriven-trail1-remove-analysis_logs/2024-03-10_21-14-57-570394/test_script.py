def even_power_sum(n):
    '''
    Write a python function that takes in an integer n and finds the sum of the first n even natural numbers that are raised to the fifth power.
    assert even_power_sum(2) == 1056
    '''
    if n <= 0:
        return 0
    else:
        total_sum = 0
        for i in range(1, n+1):
            total_sum += (2*i)**5
        return total_sum

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_Power_Sum(2), 1056)

if __name__ == '__main__':
    unittest.main()