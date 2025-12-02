# Updated Code:

def search(lst):
    '''
    Given a non-empty list of positive integers, return the greatest integer that is greater than
    zero, and has a frequency greater than or equal to the value of the integer itself.
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exists, return -1.
    '''
    # Validate input
    if not lst:
        return "Error: The input list is empty."
    for i in lst:
        if type(i) != int or i <= 0:
            return "Error: Input list should only contain positive integers"

    # Count frequency of each integer in the input list
    freq_dict = {}
    for i in lst:
        if i not in freq_dict:
            freq_dict[i] = 1
        else:
            freq_dict[i] += 1

    # Find the greatest integer that meets the frequency requirement
    result = -1
    for i in sorted(freq_dict.keys(), reverse=True):
        if freq_dict[i] >= i and i > result:
            result = i

    return result
import unittest

class TestSearch(unittest.TestCase):
    def test_search(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)
        
if __name__ == '__main__':
    unittest.main()