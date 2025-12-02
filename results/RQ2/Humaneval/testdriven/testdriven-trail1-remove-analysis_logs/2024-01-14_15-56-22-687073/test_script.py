def reverse_delete(s,c):
    """
    Task
    We are given two strings s and c, you have to delete all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """

    # Using regular expressions for more efficient and concise code
    import re

    # Delete all characters in s that are equal to any character in c
    result_list = re.sub(f'[{c}]', '', s)

    # Check if the result string is palindrome
    is_palindrome = result_list == result_list[::-1]

    return result_list, is_palindrome
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(reverse_delete("abcde", "ae"), ('bcd', False))
        
    def test2(self):
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))
        
    def test3(self):
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ('cdedc', True))

if __name__ == '__main__':
    unittest.main()