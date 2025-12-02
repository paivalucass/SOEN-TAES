def sum_of_digits(nums):
    '''Write a function to compute the sum of digits of each number of a given list.
    assert sum_of_digits([10,2,56])==14'''
    total_sum = 0
    for num in nums:
        total_sum += sum(int(digit) for digit in str(abs(num)))
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_of_digits([10,2,56]), 14)

if __name__ == '__main__':
    unittest.main()