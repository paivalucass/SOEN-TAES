def first_non_repeating_character(str1):
    from collections import Counter
    # Create a counter to count the occurrences of each character
    char_count = Counter(str1)
    
    # Iterate through the input string to find the first non-repeated character
    for char in str1:
        if char_count[char] == 1:
            return char
    
    # If no non-repeated character is found, return None
    return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_non_repeating_character('abcabc'), None)

if __name__ == '__main__':
    unittest.main()