def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    """
    if not text: # Check if string is empty
        return True
    
    text = text.lower() # Convert string to lowercase
    left = 0 # Initialize left pointer to 0
    right = len(text) - 1 # Initialize right pointer to end of string
    
    while left < right: # Loop until left pointer is greater than or equal to right pointer
        if not text[left].isalnum(): # Check if left character is alphanumeric
            left += 1 # Move left pointer one step right
        elif not text[right].isalnum(): # Check if right character is alphanumeric
            right -= 1 # Move right pointer one step left
        elif text[left] != text[right]: # Check if left and right characters are not equal
            return False
        else:
            left += 1 # Move left pointer one step right
            right -= 1 # Move right pointer one step left
            
    return True # Return True if string is palindrome
import unittest

class TestPalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character_string(self):
        self.assertTrue(is_palindrome('a'))

    def test_palindrome_string(self):
        self.assertTrue(is_palindrome('racecar'))

    def test_non_palindrome_string(self):
        self.assertFalse(is_palindrome('hello'))

if __name__ == '__main__':
    unittest.main()