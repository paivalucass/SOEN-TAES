def reverse_string_list(stringlist):
    '''Function to reverse each string in a given list of string values.'''
    if not isinstance(stringlist, list):
        raise TypeError("Input should be a list of strings")
    
    # Using list comprehension to reverse each string in the list
    reversed_list = [s[::-1] for s in stringlist]
    return reversed_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']), ['deR', 'neerG', 'eulB', 'etihW', 'kcalB'])

if __name__ == '__main__':
    unittest.main()