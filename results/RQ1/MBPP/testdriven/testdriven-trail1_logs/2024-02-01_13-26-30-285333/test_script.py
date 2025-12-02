def remove_length(test_str, K):
    '''
    Write a function to remove all the words with k length in the given string.
    assert remove_length('The person is most value tet', 3) == 'person is most value'
    '''
    # input validation
    if not isinstance(test_str, str) or not isinstance(K, int) or K < 0:
        return "Invalid input"

    words = test_str.split()
    modified_str = ' '.join([word for word in words if len(word) != K])
    return modified_str
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_length('The person is most value tet', 3), 'person is most value')

if __name__ == '__main__':
    unittest.main()