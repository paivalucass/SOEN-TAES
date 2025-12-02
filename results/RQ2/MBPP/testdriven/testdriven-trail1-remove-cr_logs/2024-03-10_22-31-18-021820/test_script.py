def string_to_list(string): 
    '''Write a function to convert a string to a list of strings split on the space character.'''
    # Error Handling:
    if not isinstance(string, str) or not string:
        return "Error: Input must be a non-empty string"
        
    # Implementation:
    word_list = string.split()
    return word_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_list('python programming'), ['python', 'programming'])

if __name__ == '__main__':
    unittest.main()