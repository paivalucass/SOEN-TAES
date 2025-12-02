def remove_lowercase(str1):
    '''Write a function to remove lowercase substrings from a given string.'''
    if not str1:
        return ""

    result = ''
    start = 0
    for i in range(len(str1)):
        if str1[i].isalpha() and str1[i].islower():  # using isalpha() to check if a character is a lowercase letter
            result += str1[start:i]
            while i < len(str1) and str1[i].isalpha() and str1[i].islower():  # using isalpha() to check if a character is a lowercase letter
                i += 1
            start = i
    result += str1[start:]
    return result

assert remove_lowercase("PYTHon")==('PYTH')  # adding a test case as per the Tester's suggestion
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_lowercase('PYTHon'), 'PYTH')

if __name__ == '__main__':
    unittest.main()