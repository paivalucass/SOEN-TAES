def max_difference(test_list):
    '''Write a function to find the maximum difference between available pairs in the given tuple list.'''
    
    if not isinstance(test_list, list):
        raise TypeError("Invalid Input Type")
    if not all(isinstance(t, tuple) and len(t) == 2 for t in test_list):
        raise TypeError("Incorrect Input Format")
        
    max_diff = 0
    for t in test_list:
        diff = abs(t[0] - t[1])
        if diff > max_diff:
            max_diff = diff
            
    return max_diff

assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]), 7)

if __name__ == '__main__':
    unittest.main()