def long_words(n, s):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(s, str):
        raise ValueError("s must be a string")

    if not s:
        return "Input string is empty"

    words = s.split()

    long_words = [word for word in words if len(word) > n]

    return long_words
import unittest

class Test(unittest.TestCase):
    def test_long_words(self):
        self.assertEqual(long_words(3, "python is a programming language"), ['python', 'programming', 'language'])

if __name__ == '__main__':
    unittest.main()