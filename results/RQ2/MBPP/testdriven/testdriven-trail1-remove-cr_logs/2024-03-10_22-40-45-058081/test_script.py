def count_element_in_list(list1, x): 
    '''
    Function to count the number of sublists containing a particular element.
    '''
    count = 0
    
    for sublist in list1:
        if x in sublist:
            count += 1
    
    return count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1), 3)

if __name__ == '__main__':
    unittest.main()