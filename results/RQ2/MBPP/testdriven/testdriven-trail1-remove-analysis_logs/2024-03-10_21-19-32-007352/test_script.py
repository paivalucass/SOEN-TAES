def check_greater(arr, number):
    '''Write a function to check whether the entered number is greater than the elements of the given array.'''
    if not isinstance(arr, list) or not all(isinstance(x, (int, float)) for x in arr) or not isinstance(number, (int, float)):
        return "Invalid input types. Please enter a list of numbers and a valid number."

    if len(arr) == 0:
        return False

    for element in arr:
        if element >= number:
            return False
    
    return True
import unittest

class Test(unittest.TestCase):
    def test_check_greater(self):
        self.assertEqual(check_greater([1, 2, 3, 4, 5], 4), False)

if __name__ == '__main__':
    unittest.main()