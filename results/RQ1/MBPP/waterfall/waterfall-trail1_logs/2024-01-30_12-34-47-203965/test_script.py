def long_words(n, word_list):
    if not isinstance(word_list, list):
        raise ValueError("Input word_list is not a list")
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input n is not a positive integer")

    result = [word for word in word_list if len(word) > n]
    return result
import unittest

class Test(unittest.TestCase):
    def test_long_words(self):
        self.assertEqual(long_words(3, "python is a programming language"), ['python', 'programming', 'language'])

if __name__ == '__main__':
    unittest.main()