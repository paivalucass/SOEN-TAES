def remove_length(test_str, K):
    if not test_str or not isinstance(K, int) or K <= 0:
        return "Invalid input"

    words = test_str.split()
    filtered_words = [word for word in words if len(word) != K]
    return ' '.join(filtered_words)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_length('The person is most value tet', 3), 'person is most value')

if __name__ == '__main__':
    unittest.main()