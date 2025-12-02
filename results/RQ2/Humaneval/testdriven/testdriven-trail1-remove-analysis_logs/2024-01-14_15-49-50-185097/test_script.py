def digitSum(s):
    """
    Task
    Write a function that takes a string as input and returns the sum of the upper characters only'\n    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    sum_of_upper_characters = 0
    for char in s:
        if char.isupper():
            sum_of_upper_characters += ord(char)
    return sum_of_upper_characters
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(digitSum(''), 0)

    def test_mixed_case_string(self):
        self.assertEqual(digitSum('abAB'), 131)
        self.assertEqual(digitSum('abcCd'), 67)
        self.assertEqual(digitSum('helloE'), 69)
        self.assertEqual(digitSum('woArBld'), 131)
        self.assertEqual(digitSum('aAaaaXa'), 153)

if __name__ == '__main__':
    unittest.main()