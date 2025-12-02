def max_sum_list(lists):
    '''Write a function that returns the list in a list of lists whose sum of elements is the highest.
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]'''
    
    if not lists or all(not sublist for sublist in lists):
        raise ValueError("Input list or sublists should not be empty")
    
    max_sum = float('-inf')
    max_sum_list = None
    
    for sublist in lists:
        if not sublist:
            continue
        
        sublist_sum = sum(sublist)
        if sublist_sum > max_sum:
            max_sum = sublist_sum
            max_sum_list = sublist
    
    return max_sum_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]), [10, 11, 12])

if __name__ == '__main__':
    unittest.main()