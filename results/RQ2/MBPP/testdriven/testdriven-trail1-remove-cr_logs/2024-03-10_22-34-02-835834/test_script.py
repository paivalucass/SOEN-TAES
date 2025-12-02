def larg_nnum(list1, n):
    '''
    Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
    
    Input:
    - list1: a list of integers
    - n: an integer representing the number of largest items to return
    
    Output:
    - Returns a list containing the n largest items from the input list
    
    Raises:
    - ValueError: if the input list is empty
    - ValueError: if the value of n is greater than the length of the input list
    '''

    if len(list1) == 0:
        raise ValueError("Input list cannot be empty")

    if n > len(list1):
        raise ValueError("Value of n cannot be greater than the length of the input list")

    sorted_list = sorted(list1, reverse=True)
    return sorted_list[:n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2), [100, 90])

if __name__ == '__main__':
    unittest.main()