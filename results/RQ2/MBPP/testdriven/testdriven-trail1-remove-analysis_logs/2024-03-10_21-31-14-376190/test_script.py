def max_sum_list(lists):
    '''Write a function that returns the list in a list of lists whose sum of elements is the highest.
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]'''
    if not lists:
        return []
    
    max_sum = float('-inf')
    max_list = []
    
    for l in lists:
        if all(isinstance(item, int) for item in l):
            if sum(l) > max_sum:
                max_sum = sum(l)
                max_list = l
        else:
            raise ValueError("Input list should only contain integers")

    return max_list
import unittest

class Test(unittest.TestCase):
    def test_max_sum_list(self):
        self.assertEqual(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]), [10, 11, 12])

if __name__ == '__main__':
    unittest.main()