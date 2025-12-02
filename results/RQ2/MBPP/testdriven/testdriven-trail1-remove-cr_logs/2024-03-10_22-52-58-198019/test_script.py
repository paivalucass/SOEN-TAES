def remove_length(test_str, K):
    '''
    Write a function to remove all the words with k length in the given string.
    Inputs:
    - test_str: the input string
    - K: the length of words to be removed
    '''
    # Error handling for empty input string or negative length K
    if len(test_str) == 0 or K < 0:
        return "Error: Invalid input"

    # Split the input string into individual words
    words_list = test_str.split()
    
    # Iterate through the words to check their length and remove words with length K
    words_list = [word for word in words_list if len(word) != K]
    
    # Join the list of words back into a string
    result_str = ' '.join(words_list)
    
    return result_str

assert remove_length('The person is most value tet', 3) == 'person is most value'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_length('The person is most value tet', 3), 'person is most value')

if __name__ == '__main__':
    unittest.main()