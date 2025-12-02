def freq_count(list1):
    '''Write a function to get the frequency of all the elements in a list, returned as a dictionary.'''
    # Input validation
    if not isinstance(list1, list) or not all(isinstance(x, int) for x in list1) or len(list1) == 0:
        raise ValueError("Input should be a non-empty list containing only integers")
    
    # Implementation details for handling edge cases and error handling
    # ...
    frequency_dictionary = {}
    for item in list1:
        if item in frequency_dictionary:
            frequency_dictionary[item] += 1
        else:
            frequency_dictionary[item] = 1
    return frequency_dictionary

# Test Cases:
def test_freq_count():
    assert freq_count([1,1,2,2,2,3,4,4,4,4]) == {1: 2, 2: 3, 3: 1, 4: 4}
    assert freq_count([]) == {}
    try:
        freq_count(['a', 1, 2, 3, 'b'])
    except ValueError as e:
        assert str(e) == "Input should be a non-empty list containing only integers"
    assert freq_count([1,2,3]) == {1: 1, 2: 1, 3: 1}
    try:
        freq_count({1, 2, 3})
    except ValueError as e:
        assert str(e) == "Input should be a non-empty list containing only integers"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]), {10: 4, 20: 4, 40: 2, 50: 2, 30: 1})

if __name__ == '__main__':
    unittest.main()