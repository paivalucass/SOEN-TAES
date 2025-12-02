def remove_length(test_str, K):
    if not isinstance(K, int) or K <= 0:
        raise ValueError("K must be a positive integer")

    if not test_str:
        return test_str

    words = test_str.split()
    modified_words = [word for word in words if len(word) != K]
    return ' '.join(modified_words)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_length('The person is most value tet', 3), 'person is most value')

if __name__ == '__main__':
    unittest.main()