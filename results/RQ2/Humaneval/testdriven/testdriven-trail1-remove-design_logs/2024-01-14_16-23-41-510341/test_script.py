def words_string(s):
    return [word for word in s.replace(",","").split(" ") if word]
import unittest

class Test(unittest.TestCase):
    def test_words_string(self):
        self.assertEqual(words_string("Hi, my name is John"), ["Hi", "my", "name", "is", "John"])
        self.assertEqual(words_string("One, two, three, four, five, six"), ["One", "two", "three", "four", "five", "six"])

if __name__ == '__main__':
    unittest.main()