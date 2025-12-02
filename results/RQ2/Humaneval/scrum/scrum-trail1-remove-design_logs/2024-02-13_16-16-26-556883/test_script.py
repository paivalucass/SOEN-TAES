def words_string(s):
    import re
    return re.split(r', | ', s)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(words_string("Hi, my name is John"), ["Hi", "my", "name", "is", "John"])
        self.assertEqual(words_string("One, two, three, four, five, six"), ["One", "two", "three", "four", "five", "six"])

if __name__ == '__main__':
    unittest.main()