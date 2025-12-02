def digitSum(s):
    """
    Task
    Write a function that takes a string as input and returns the sum of the ASCII codes of the uppercase characters only.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    # Initialize the sum of ASCII codes of uppercase characters
    upper_sum = 0
    
    # Iterate through each character in the input string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # Add the ASCII code of the uppercase character to the sum
            upper_sum += ord(char)  
    # Return the sum of ASCII codes of uppercase characters
    return upper_sum
import unittest

class Test(unittest.TestCase):
    def test_digitSum_emptyString(self):
        self.assertEqual(digitSum(''), 0)
    
    def test_digitSum_abAB(self):
        self.assertEqual(digitSum('abAB'), 131)
    
    def test_digitSum_abcCd(self):
        self.assertEqual(digitSum('abcCd'), 67)
    
    def test_digitSum_helloE(self):
        self.assertEqual(digitSum('helloE'), 69)
    
    def test_digitSum_woArBld(self):
        self.assertEqual(digitSum('woArBld'), 131)
    
    def test_digitSum_aAaaaXa(self):
        self.assertEqual(digitSum('aAaaaXa'), 153)

if __name__ == '__main__':
    unittest.main()