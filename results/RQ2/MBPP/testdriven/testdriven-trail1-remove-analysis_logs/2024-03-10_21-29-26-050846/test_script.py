def odd_num_sum(n):
    sum_of_fourth_powers = 0
    for odd_num in range(1, 2*n+1, 2):
        sum_of_fourth_powers += odd_num**4
    return sum_of_fourth_powers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_num_sum(2), 82)

if __name__ == '__main__':
    unittest.main()