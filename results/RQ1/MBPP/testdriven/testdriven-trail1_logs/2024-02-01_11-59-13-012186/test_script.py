def find_substring(str_list, substring):
    '''Write a function to check if a substring is present in a given list of strings.'''
    if not isinstance(str_list, list) or not all(isinstance(s, str) for s in str_list):
        raise ValueError("str_list must be a list of strings")

    if not isinstance(substring, str):
        raise ValueError("substring must be a string")

    for string in str_list:
        if substring in string:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_substring(["red", "black", "white", "green", "orange"],"ack"), True)

if __name__ == '__main__':
    unittest.main()