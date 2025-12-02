def count_char_position(str1): 
    '''Write a function to count the number of characters in a string that occur at the same position in the string as in the English alphabet (case insensitive).
    assert count_char_position("xbcefg") == 2'''
    
    # Check if input string is empty
    if not str1:
        return "Error: Input string is empty"
    
    count = 0
    # Iterate through the characters in the input string
    for i in range(len(str1)):
        char = str1[i].lower()
        # Check if the character is an alphabet and occurs at the same position as its index in the English alphabet
        if char.isalpha() and ord(char) - ord('a') == i:
            count += 1
    
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_char_position('xbcefg'), 2)

if __name__ == '__main__':
    unittest.main()