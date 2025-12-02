def filter_oddnumbers(nums):
    '''Write a function to filter odd numbers.'''
    result = []
    for num in nums:
        if num % 2 != 0:
            result.append(num)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 3, 5, 7, 9])

if __name__ == '__main__':
    unittest.main()