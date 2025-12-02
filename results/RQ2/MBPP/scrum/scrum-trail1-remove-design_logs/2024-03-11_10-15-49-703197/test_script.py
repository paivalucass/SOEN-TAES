def replace_blank(str1, char):
    new_str = ""
    for c in str1:
        if c == " ":
            new_str += char
        else:
            new_str += c
    return new_str

'''
Test Cases:
assert replace_blank("", "@") == "@"
assert replace_blank("hello", "@") == "hello"
assert replace_blank("hello  people", "@") == "hello@@people"
assert replace_blank("hello!@people", "@") == "hello!@people"
'''
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_blank('hello people', '@'), 'hello@people')

if __name__ == '__main__':
    unittest.main()