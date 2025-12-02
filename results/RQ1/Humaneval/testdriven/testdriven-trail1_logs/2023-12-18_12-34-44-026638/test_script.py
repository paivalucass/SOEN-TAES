def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    words = [w.strip() for word in s.split(",") for w in word.split()]
    return words
import unittest

class Test(unittest.TestCase):
    def test_words_string(self):
        self.assertEqual(words_string("Hi, my name is John"), ["Hi", "my", "name", "is", "John"])
        self.assertEqual(words_string("One, two, three, four, five, six"), ["One", "two", "three", "four", "five", "six"])

if __name__ == '__main__':
    unittest.main()