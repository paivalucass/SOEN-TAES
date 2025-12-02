def long_words(n, string):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a positive integer")
    if not string:
        raise ValueError("string cannot be empty")

    words = string.split()
    return [word for word in words if len(word) > n]
import unittest

class Test(unittest.TestCase):
    def test_long_words(self):
        self.assertEqual(long_words(3, "python is a programming language"), ['python', 'programming', 'language'])

if __name__ == '__main__':
    unittest.main()