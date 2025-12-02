def freq_count(list1):
    '''
    Function to get the frequency of all the elements in a list, returned as a dictionary.
    Input: list of elements
    Output: dictionary with elements as keys and their frequencies as values
    '''
    if not isinstance(list1, list):
        raise ValueError("Input should be a list")
    
    freq_dict = {}
    for item in list1:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]), {10: 4, 20: 4, 40: 2, 50: 2, 30: 1})

if __name__ == '__main__':
    unittest.main()