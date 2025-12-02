def remove_length(test_str, K):
    if not isinstance(test_str, str) or not isinstance(K, int) or K < 0:
        return "Invalid input"
    
    words = test_str.split()
    result = [word for word in words if len(word) != K]
    return ' '.join(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_length('The person is most value tet', 3), 'person is most value')

if __name__ == '__main__':
    unittest.main()