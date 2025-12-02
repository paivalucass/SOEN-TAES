def diff_even_odd(list1):
    if len(list1) == 0:
        return "Error: Input list is empty"
    
    for index, value in enumerate(list1):
        if not isinstance(value, int):
            return f"Error: Non-numeric value '{value}' at index {index}"
    
    even_numbers = [num for num in list1 if num % 2 == 0]
    odd_numbers = [num for num in list1 if num % 2 != 0]
    
    if len(even_numbers) == 0 or len(odd_numbers) == 0:
        return "Error: No even or odd numbers in the list"
    
    if len(even_numbers) == len(list1) or len(odd_numbers) == len(list1):
        return "Error: All numbers in the list are of the same type (even or odd)"
    
    diff = even_numbers[0] - odd_numbers[0]
    return diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(diff_even_odd([1,3,5,7,4,1,6,8]), 3)

if __name__ == '__main__':
    unittest.main()