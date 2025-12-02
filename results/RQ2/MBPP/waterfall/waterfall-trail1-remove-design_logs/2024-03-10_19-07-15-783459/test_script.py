def long_words(n, string):
    if not string or n < 0:
        return "Invalid input"
    
    word_list = string.split()
    return [word for word in word_list if len(word) > n]
import unittest

class Test(unittest.TestCase):
    def test_long_words(self):
        self.assertEqual(long_words(3, "python is a programming language"), ['python', 'programming', 'language'])

if __name__ == '__main__':
    unittest.main()