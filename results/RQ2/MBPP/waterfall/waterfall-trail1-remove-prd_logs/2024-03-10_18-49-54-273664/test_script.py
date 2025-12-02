def sum_in_range(l, r): 
    '''Write a python function to find the sum of all odd natural numbers within the range l and r.'''
    if not isinstance(l, int) or not isinstance(r, int) or l < 0 or r < 0 or l > r:
        raise ValueError("Input parameters must be natural numbers with l <= r")

    total_sum = 0
    for num in range(l, r + 1):
        if num % 2 != 0:
            total_sum += num

    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_odd(5), 4)

if __name__ == '__main__':
    unittest.main()