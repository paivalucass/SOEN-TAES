def long_words(n, s):
    if not isinstance(n, int) or n <= 0:
        return "Error: n should be a positive integer"
    if not isinstance(s, str) or len(s) == 0:
        return "Error: s should be a non-empty string"
    
    words = s.split()
    long_words = [word for word in words if len(word) > n]
    return long_words
import unittest

class Test(unittest.TestCase):
    def test_long_words(self):
        self.assertEqual(long_words(3, "python is a programming language"), ['python', 'programming', 'language'])

if __name__ == '__main__':
    unittest.main()