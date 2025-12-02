def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''

    # Create a frequency list to store the count of each integer
    frequency_list = [0] * (max(lst) + 1)
    
    # Calculate the frequency of each integer in the list
    for num in lst:
        frequency_list[num] += 1
    
    # Find the greatest integer that has a frequency greater than or equal to its value
    max_val = -1
    for i in range(1, len(frequency_list)):
        if frequency_list[i] >= i:
            max_val = max(max_val, i)
    
    return max_val
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)

    def test_2(self):
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test_3(self):
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

if __name__ == '__main__':
    unittest.main()