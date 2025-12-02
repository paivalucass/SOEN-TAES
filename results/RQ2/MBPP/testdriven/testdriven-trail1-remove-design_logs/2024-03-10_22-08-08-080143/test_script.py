def check_greater(arr, number):
    '''
    Write a function to check whether the entered number is greater than the elements of the given array.
    
    Parameters:
    arr (list): The input array
    number (int): The number to compare against
    
    Returns:
    bool: True if all elements are less than the given number, False otherwise
    '''
    return all(num < number for num in arr)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_greater([1, 2, 3, 4, 5], 4), False)

if __name__ == '__main__':
    unittest.main()