def swap_list(new_list):
    '''Interchanges the first and last elements of the input list and returns the modified list.'''
    
    if not isinstance(new_list, list):
        raise ValueError("Input should be a list")
    
    if len(new_list) < 2:
        raise ValueError("Input list should have at least two elements")
    
    new_list[0], new_list[-1] = new_list[-1], new_list[0]  # Swap the first and last elements
    
    return new_list

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(swap_List([12, 35, 9, 56, 24]), [24, 35, 9, 56, 12])

if __name__ == '__main__':
    unittest.main()