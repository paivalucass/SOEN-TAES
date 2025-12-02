def reverse_vowels(str1):
    if str1 is None or len(str1) == 0:
        return str1
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    str_list = list(str1)
    left, right = 0, len(str_list) - 1
    
    while left < right:
        while str_list[left].lower() not in vowels and left < right:
            left += 1
        while str_list[right].lower() not in vowels and left < right:
            right -= 1
        str_list[left], str_list[right] = str_list[right], str_list[left]
        left += 1
        right -= 1
    
    return ''.join(str_list)

# Test Cases:
{
  "requirement analysis": "analysis",
  "test_cases": [
    {
      "Test Title": "Valid input with vowels to reverse",
      "Input Data": "parameter1='Python'",
      "Expected Output": "Pthyon"
    },
    {
      "Test Title": "Valid input with no vowels to reverse",
      "Input Data": "parameter1='Rhythm'",
      "Expected Output": "Rhythm"
    },
    {
      "Test Title": "Empty input string",
      "Input Data": "parameter1=''",
      "Expected Output": ""
    },
    {
      "Test Title": "Boundary test case with max length input string",
      "Input Data": "parameter1='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'",
      "Expected Output": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    },
    {
      "Test Title": "Boundary test case with null input",
      "Input Data": "parameter1=None",
      "Expected Output": "None"
    },
    {
      "Test Title": "Negative test case with invalid input data type",
      "Input Data": "parameter1=123",
      "Expected Output": "123"
    },
    {
      "Test Title": "Negative test case with non-string input",
      "Input Data": "parameter1=12345",
      "Expected Output": "12345"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_reverse_vowels(self):
        self.assertEqual(reverse_vowels("Python"), "Python")

if __name__ == '__main__':
    unittest.main()