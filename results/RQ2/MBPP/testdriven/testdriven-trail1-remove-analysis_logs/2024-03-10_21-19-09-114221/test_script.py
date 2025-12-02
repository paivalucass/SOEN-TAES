def filter_oddnumbers(nums):
    '''Write a function to filter odd numbers.
    assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]'''
    
    if not nums:
        raise ValueError("Input list cannot be empty")

    if not all(isinstance(num, int) for num in nums):
        raise ValueError("Input list should only contain integers")

    odd_numbers = [num for num in nums if num % 2 != 0]
    return odd_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 3, 5, 7, 9])

if __name__ == '__main__':
    unittest.main()