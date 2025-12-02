import re

def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.

    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """

    if s is None or s.strip() == "":
        return []

    words = [word.strip() for word in re.split(r'[,\s]+', s)]
    return [word for word in words if word]

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(words_string("Hi, my name is John"), ["Hi", "my", "name", "is", "John"])
        self.assertEqual(words_string("One, two, three, four, five, six"), ["One", "two", "three", "four", "five", "six"])

if __name__ == '__main__':
    unittest.main()