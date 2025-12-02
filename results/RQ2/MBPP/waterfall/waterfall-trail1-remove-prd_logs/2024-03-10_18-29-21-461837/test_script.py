def long_words(n, input_string):
    word_list = input_string.split()
    long_words_list = [word for word in word_list if len(word) > n]
    return long_words_list
import unittest

class Test(unittest.TestCase):
    def test_long_words(self):
        self.assertEqual(long_words(3, "python is a programming language"), ['python','programming','language'])

if __name__ == '__main__':
    unittest.main()