def remove_length(test_str, K):
    words = test_str.split()
    filtered_words = [word for word in words if len(word) != K]
    result = " ".join(filtered_words)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_length('The person is most value tet', 3), 'person is most value')

if __name__ == '__main__':
    unittest.main()