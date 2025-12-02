def max_run_uppercase(test_str):
    '''Write a function to find maximum run of uppercase characters in the given string.'''
    max_run = 0
    current_run = 0

    if test_str == '':
        return "Error: Input string is empty"

    for char in test_str:
        if char.isupper():
            current_run += 1
            if current_run > max_run:
                max_run = current_run
        else:
            current_run = 0

    return max_run
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_run_uppercase('GeMKSForGERksISBESt'), 5)

if __name__ == '__main__':
    unittest.main()