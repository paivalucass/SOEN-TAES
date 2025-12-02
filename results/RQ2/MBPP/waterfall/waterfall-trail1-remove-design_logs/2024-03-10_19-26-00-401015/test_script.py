def remove_length(test_str, K):
    return ' '.join(word for word in test_str.split() if len(word) != K)
import unittest

class Test(unittest.TestCase):
    def test_remove_length(self):
        self.assertEqual(remove_length('The person is most value tet', 3), 'person is most value')

if __name__ == '__main__':
    unittest.main()