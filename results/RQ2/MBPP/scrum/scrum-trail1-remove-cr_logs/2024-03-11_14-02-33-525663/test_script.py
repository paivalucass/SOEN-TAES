def remove_length(test_str, K):
    if not test_str:
        raise ValueError("Input string cannot be empty")

    if K < 0:
        raise ValueError("Length of words to remove cannot be negative")

    words = test_str.split()
    remaining_words = [word for word in words if len(word) != K]
    new_str = " ".join(remaining_words)
    return new_str
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_length('The person is most value tet', 3), 'person is most value')

if __name__ == '__main__':
    unittest.main()