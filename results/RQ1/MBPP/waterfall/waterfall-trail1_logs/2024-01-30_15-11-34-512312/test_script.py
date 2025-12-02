def mul_even_odd(list1):
    if not isinstance(list1, list):
        raise TypeError("Input should be a list of numbers")
    
    if len(list1) < 2:
        return None
    
    even_numbers = [num for num in list1 if num % 2 == 0 and num != 0]
    odd_numbers = [num for num in list1 if num % 2 != 0]
    
    if len(even_numbers) == 0 or len(odd_numbers) == 0:
        raise ValueError("No even or odd number found in the list")
    
    product = even_numbers[0] * odd_numbers[0]
    return product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mul_even_odd([1,3,5,7,4,1,6,8]), 4)

if __name__ == '__main__':
    unittest.main()