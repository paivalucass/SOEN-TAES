def odd_num_sum(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    
    odd_numbers = [i for i in range(1, 2*n, 2)]
    sum_of_fourth_powers = sum([i**4 for i in odd_numbers])
    
    return sum_of_fourth_powers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_num_sum(2), 82)

if __name__ == '__main__':
    unittest.main()