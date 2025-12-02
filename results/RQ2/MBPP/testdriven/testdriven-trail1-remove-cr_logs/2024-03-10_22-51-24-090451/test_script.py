def capital_words_spaces(str1):
    '''Write a function to put spaces between words starting with capital letters in a given string.'''
    
    # Write your code here
    
    return str1  # Replace with the modified string with spaces between words starting with capital letters
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(capital_words_spaces('Python'), 'Python')

if __name__ == '__main__':
    unittest.main()