def remove_length(test_str, K):
    if not isinstance(test_str, str):
        raise ValueError("Input string should be a valid string")

    if not test_str:
        return ""

    if K < 0:
        raise ValueError("K should be a non-negative integer")

    words = test_str.split()
    new_words = [word for word in words if len(word) != K]
    
    if len(new_words) == 0:
        raise ValueError("No words of length K found in the input string")

    return ' '.join(new_words)
import unittest

class Test(unittest.TestCase):
    def test_remove_length(self):
        self.assertEqual(remove_length('The person is most value tet', 3), 'person is most value')

if __name__ == '__main__':
    unittest.main()