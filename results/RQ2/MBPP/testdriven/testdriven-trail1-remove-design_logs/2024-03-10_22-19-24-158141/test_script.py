def mul_even_odd(list1):
    '''Write a function to find the product of the first even and odd numbers in a given list.'''
    even_numbers = [num for num in list1 if num % 2 == 0]
    odd_numbers = [num for num in list1 if num % 2 != 0]
    if len(even_numbers) == 0:
        return "Error: No even number found in the list"
    if len(odd_numbers) == 0:
        return "Error: No odd number found in the list"
    return even_numbers[0] * odd_numbers[0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mul_even_odd([1,3,5,7,4,1,6,8]), 4)

if __name__ == '__main__':
    unittest.main()