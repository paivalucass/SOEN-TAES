def split_words(txt):
    if ' ' in txt:
        return split_by_space(txt)
    elif ',' in txt:
        return split_by_comma(txt)
    else:
        return count_lower_odd_chars(txt)

def split_by_space(txt):
    return txt.split()

def split_by_comma(txt):
    return txt.split(',')

def count_lower_odd_chars(txt):
    count = sum(1 for char in txt if char.islower() and ord(char) % 2 != 0)
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test('Hello world!'), ["Hello", "world!"])
        self.assertEqual(function_under_test('Hello,world!'), ["Hello", "world!"])
        self.assertEqual(function_under_test('abcdef'), 3)

if __name__ == '__main__':
    unittest.main()