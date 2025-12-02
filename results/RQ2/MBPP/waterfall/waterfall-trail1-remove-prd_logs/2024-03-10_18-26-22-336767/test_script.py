def recursive_list_sum(data_list):
    '''Write a function to flatten a list and sum all of its elements.'''
    if not isinstance(data_list, list):
        raise TypeError("Input is not a list")
    
    total_sum = 0
    for element in data_list:
        if isinstance(element, list):
            total_sum += recursive_list_sum(element)
        elif isinstance(element, int):
            total_sum += element
        else:
            raise TypeError("List contains non-integer elements")
    
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(recursive_list_sum([1, 2, [3,4],[5,6]]), 21)

if __name__ == '__main__':
    unittest.main()