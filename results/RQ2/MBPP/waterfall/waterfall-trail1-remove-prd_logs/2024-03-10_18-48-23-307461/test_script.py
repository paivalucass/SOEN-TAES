def odd_num_sum(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    odd_numbers = [i for i in range(1, 2*n, 2)]
    sum_of_fourth_power = sum([num**4 for num in odd_numbers])

    return sum_of_fourth_power
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_num_sum(2), 82)

if __name__ == '__main__':
    unittest.main()