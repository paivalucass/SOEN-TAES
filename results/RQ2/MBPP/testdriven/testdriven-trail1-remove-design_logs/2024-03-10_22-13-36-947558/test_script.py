def reverse_words(s):
    '''Write a function to reverse words separated by spaces in a given string.
    assert reverse_words("python program")==("program python")'''
    
    # Use list comprehension for better performance and readability
    words = [word for word in s.split()]
    
    # Reverse the list of words and join them back into a string
    reversed_words = ' '.join(reversed(words))
    
    return reversed_words
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_words('python program'), 'program python')

if __name__ == '__main__':
    unittest.main()