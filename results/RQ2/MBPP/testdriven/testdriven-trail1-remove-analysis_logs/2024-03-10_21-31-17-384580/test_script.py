def max_run_uppercase(test_str):
    '''
    Write a function to find maximum run of uppercase characters in the given string.
    assert max_run_uppercase('GeMKSForGERksISBESt') == 5
    '''
    # Initialize variables to keep track of maximum run and current run
    max_run = 0
    current_run = 0
    
    # Iterate through the string to find the maximum run of uppercase characters
    for char in test_str:
        if char.isupper():
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0
    
    # Return the maximum run of uppercase characters
    return max_run
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_run_uppercase('GeMKSForGERksISBESt'), 5)

if __name__ == '__main__':
    unittest.main()