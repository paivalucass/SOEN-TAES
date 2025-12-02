def split_words(txt):
    import re
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return [i for i in txt.split(',') if i]
    else:
        count = len([c for c in txt if c.islower() and ord(c) % 2 != 0])
        return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test('Hello world!'), ['Hello', 'world!'])
        self.assertEqual(function_under_test('Hello,world!'), ['Hello', 'world!'])
        self.assertEqual(function_under_test('abcdef'), 3)

if __name__ == '__main__':
    unittest.main()