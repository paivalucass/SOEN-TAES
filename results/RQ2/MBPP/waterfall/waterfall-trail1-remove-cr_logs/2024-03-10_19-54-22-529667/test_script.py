def long_words(min_length, word_list):
    result = []
    if isinstance(word_list, str):
        word_list = word_list.split()
    elif not isinstance(word_list, list):
        raise TypeError("word_list should be a string or a list")

    for word in word_list:
        if len(word) > min_length:
            result.append(word)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_long_words(self):
        self.assertEqual(long_words(3, "python is a programming language"), ['python', 'programming', 'language'])

if __name__ == '__main__':
    unittest.main()