def long_words(n, words):
    result = []
    word_list = words.split()
    for word in word_list:
        if len(word) > n:
            result.append(word)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(long_words(3, "python is a programming language"), ['python', 'programming', 'language'])

if __name__ == '__main__':
    unittest.main()